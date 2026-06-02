#!/usr/bin/env python
"""Check key-claim and key-number ledger completeness."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = (
    "claim_id",
    "claim_or_number",
    "claim_type",
    "source_ids",
    "source_role",
    "can_support",
    "cannot_support",
    "allowed_wording",
    "required_citation_marker",
    "final_treatment",
)


def load_data(path: Path) -> Any:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        return json.loads(text)
    try:
        import yaml  # type: ignore
    except Exception as exc:  # pragma: no cover
        raise SystemExit(f"YAML input requires PyYAML: {exc}") from exc
    return yaml.safe_load(text)


def find_entries(data: Any) -> list[dict[str, Any]]:
    if isinstance(data, list):
        return [item for item in data if isinstance(item, dict)]
    if not isinstance(data, dict):
        raise SystemExit("Key-claim ledger must be a mapping or list.")
    for key in ("key_claim_ledger", "key_claims", "claims", "material_claims"):
        value = data.get(key)
        if isinstance(value, list):
            return [item for item in value if isinstance(item, dict)]
    raise SystemExit("No key_claim_ledger list found.")


def is_empty(value: Any) -> bool:
    return value is None or value == "" or value == [] or value == {}


def check(path: Path) -> dict[str, Any]:
    entries = find_entries(load_data(path))
    errors: list[dict[str, str]] = []
    warnings: list[dict[str, str]] = []
    results: list[dict[str, Any]] = []

    for index, entry in enumerate(entries, 1):
        claim_id = str(entry.get("claim_id") or f"entry-{index}")
        material = entry.get("material", True)
        if str(material).lower() in {"false", "no", "0"}:
            continue
        missing = [field for field in REQUIRED_FIELDS if is_empty(entry.get(field))]
        if missing:
            errors.append({"type": "material_claim_missing_fields", "claim_id": claim_id, "fields": ",".join(missing)})
        if is_empty(entry.get("source_date")) and is_empty(entry.get("coverage_period")):
            errors.append({"type": "missing_source_date_or_coverage_period", "claim_id": claim_id})
        claim_type = str(entry.get("claim_type") or "").lower().replace(" ", "_")
        if claim_type in {"forecast", "model_estimate", "scenario", "announcement", "company_claim", "official_claim"}:
            if is_empty(entry.get("unsafe_overclaim_wording")):
                warnings.append({"type": "missing_unsafe_overclaim_wording", "claim_id": claim_id})
        if is_empty(entry.get("scope")):
            warnings.append({"type": "missing_scope", "claim_id": claim_id})
        results.append({"claim_id": claim_id, "missing": missing})

    if not entries:
        errors.append({"type": "empty_key_claim_ledger", "claim_id": "ledger"})

    return {"ok": not errors, "path": str(path), "entries_checked": len(results), "results": results, "errors": errors, "warnings": warnings}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check key-claim/key-number ledger completeness.")
    parser.add_argument("ledger_file", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    result = check(args.ledger_file)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(("PASS" if result["ok"] else "FAIL") + f": {args.ledger_file}")
        for error in result["errors"]:
            print(f"- error: {error['type']} {error.get('claim_id', '')} {error.get('fields', '')}".rstrip())
        for warning in result["warnings"]:
            print(f"- warning: {warning['type']} {warning.get('claim_id', '')}".rstrip())
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
