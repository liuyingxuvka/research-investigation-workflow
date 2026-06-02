#!/usr/bin/env python
"""Check structural claim/source semantic-fit risks.

This helper flags common structural mismatches only. LogicGuard still owns
exact semantic review of final wording.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


SCOPE_RANK = {
    "actor_specific": 0,
    "pilot": 0,
    "local": 1,
    "regional": 2,
    "national": 3,
    "global": 4,
}

INTERMEDIATE_PRICE_LAYERS = {"planning", "forecast", "wholesale", "capacity", "transmission", "resource_procurement"}
TERMINAL_PRICE_LAYERS = {"retail", "terminal", "user_facing", "stakeholder"}
ANNOUNCEMENT_ROLES = {"announcement", "source_statement", "company_claim", "official_claim", "context", "motive", "interpretation", "expert_interpretation"}
OUTCOME_CLAIM_TYPES = {"execution", "implementation", "operation", "outcome", "impact", "adoption", "retail_price", "stakeholder_impact"}
FORECAST_SOURCE_TYPES = {"forecast", "model_estimate", "scenario", "announcement", "company_claim"}


def load_data(path: Path) -> Any:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        return json.loads(text)
    try:
        import yaml  # type: ignore
    except Exception as exc:  # pragma: no cover
        raise SystemExit(f"YAML input requires PyYAML: {exc}") from exc
    return yaml.safe_load(text)


def normalize(value: Any) -> str:
    return str(value or "").strip().lower().replace(" ", "_").replace("-", "_")


def find_entries(data: Any) -> list[dict[str, Any]]:
    if isinstance(data, list):
        return [item for item in data if isinstance(item, dict)]
    if not isinstance(data, dict):
        raise SystemExit("Semantic-fit ledger must be a mapping or list.")
    for key in ("semantic_source_fit", "claim_support_fit", "fit_checks", "claims"):
        value = data.get(key)
        if isinstance(value, list):
            return [item for item in value if isinstance(item, dict)]
    raise SystemExit("No semantic_source_fit list found.")


def has_bridge(entry: dict[str, Any]) -> bool:
    return normalize(entry.get("bridge_evidence")) in {"yes", "true", "found", "supported", "complete"}


def check(path: Path) -> dict[str, Any]:
    entries = find_entries(load_data(path))
    errors: list[dict[str, str]] = []
    warnings: list[dict[str, str]] = []
    results: list[dict[str, Any]] = []

    for index, entry in enumerate(entries, 1):
        claim_id = str(entry.get("claim_id") or entry.get("artifact_unit") or f"entry-{index}")
        bridge = has_bridge(entry)
        claim_scope = normalize(entry.get("claim_scope"))
        source_scope = normalize(entry.get("source_scope"))
        if claim_scope in SCOPE_RANK and source_scope in SCOPE_RANK and SCOPE_RANK[claim_scope] > SCOPE_RANK[source_scope] and not bridge:
            errors.append({"type": "scope_mismatch_without_bridge", "claim_id": claim_id, "claim_scope": claim_scope, "source_scope": source_scope})

        claim_time = normalize(entry.get("claim_time") or entry.get("claim_tense") or entry.get("claim_type"))
        source_type = normalize(entry.get("source_type") or entry.get("source_status") or entry.get("source_claim_type"))
        if claim_time in {"observed", "observed_fact", "happened", "current_fact"} and source_type in FORECAST_SOURCE_TYPES and not bridge:
            errors.append({"type": "tense_mismatch_without_bridge", "claim_id": claim_id, "claim_time": claim_time, "source_type": source_type})

        claim_type = normalize(entry.get("claim_type"))
        source_role = normalize(entry.get("source_role"))
        if claim_type in OUTCOME_CLAIM_TYPES and source_role in ANNOUNCEMENT_ROLES and not bridge:
            errors.append({"type": "execution_or_outcome_mismatch_without_bridge", "claim_id": claim_id, "claim_type": claim_type, "source_role": source_role})

        claim_layer = normalize(entry.get("claim_effect_layer"))
        source_layer = normalize(entry.get("source_effect_layer"))
        if claim_layer in TERMINAL_PRICE_LAYERS and source_layer in INTERMEDIATE_PRICE_LAYERS and not bridge:
            errors.append({"type": "price_or_effect_layer_mismatch_without_bridge", "claim_id": claim_id, "claim_layer": claim_layer, "source_layer": source_layer})

        status = normalize(entry.get("status"))
        if status in {"blocked", "fail", "failed", "error"}:
            errors.append({"type": "declared_blocked_fit", "claim_id": claim_id, "status": status})
        elif status in {"warning", "partial", "unknown"}:
            warnings.append({"type": "declared_partial_fit", "claim_id": claim_id, "status": status})

        results.append({"claim_id": claim_id, "bridge_evidence": bridge})

    if not entries:
        errors.append({"type": "empty_semantic_source_fit_ledger", "claim_id": "ledger"})

    return {"ok": not errors, "path": str(path), "entries_checked": len(results), "results": results, "errors": errors, "warnings": warnings}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check structural claim/source fit risks.")
    parser.add_argument("fit_file", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    result = check(args.fit_file)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(("PASS" if result["ok"] else "FAIL") + f": {args.fit_file}")
        for error in result["errors"]:
            print(f"- error: {error['type']} {error.get('claim_id', '')}".rstrip())
        for warning in result["warnings"]:
            print(f"- warning: {warning['type']} {warning.get('claim_id', '')}".rstrip())
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
