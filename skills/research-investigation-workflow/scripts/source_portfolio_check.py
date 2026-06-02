#!/usr/bin/env python
"""Check source portfolio coverage for research investigations."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


DEFAULT_REQUIRED_CLASSES = (
    "primary_or_closest_available_record",
    "independent_or_third_party_record",
    "counter_or_limiting_record",
)

PASS_VALUES = {"complete", "covered", "found", "read", "anchored", "not_applicable", "not-applicable"}
BLOCK_VALUES = {"gap", "blocked", "access_gap", "access-gap", "not_run", "not-run", "missing", "unknown", ""}


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


def find_portfolio(data: Any) -> list[dict[str, Any]]:
    if isinstance(data, list):
        return [item for item in data if isinstance(item, dict)]
    if not isinstance(data, dict):
        raise SystemExit("Source portfolio must be a mapping or list.")
    for key in ("source_portfolio", "portfolio", "source_classes"):
        value = data.get(key)
        if isinstance(value, list):
            return [item for item in value if isinstance(item, dict)]
    nested = data.get("sourceguard") or data.get("source_guard")
    if isinstance(nested, dict):
        value = nested.get("source_portfolio")
        if isinstance(value, list):
            return [item for item in value if isinstance(item, dict)]
    raise SystemExit("No source_portfolio list found.")


def check(path: Path, required_classes: tuple[str, ...]) -> dict[str, Any]:
    rows = find_portfolio(load_data(path))
    by_class = {normalize(row.get("source_class") or row.get("class")): row for row in rows}
    errors: list[dict[str, str]] = []
    warnings: list[dict[str, str]] = []
    results: list[dict[str, Any]] = []

    for required in required_classes:
        key = normalize(required)
        row = by_class.get(key)
        if row is None:
            errors.append({"type": "required_source_class_missing", "source_class": required})
            results.append({"source_class": required, "status": "missing", "passed": False})
            continue
        status = normalize(row.get("status"))
        passed = status in PASS_VALUES
        results.append({"source_class": required, "status": status, "passed": passed})
        if not passed or status in BLOCK_VALUES:
            errors.append({"type": "required_source_class_not_covered", "source_class": required, "status": status})

    for row in rows:
        source_class = normalize(row.get("source_class") or row.get("class"))
        status = normalize(row.get("status"))
        required_value = normalize(row.get("required"))
        lineage = normalize(row.get("source_lineage_risk"))
        independence = normalize(row.get("independence_status"))
        if required_value in {"true", "yes", "required"} and status not in PASS_VALUES:
            errors.append({"type": "declared_required_class_not_covered", "source_class": source_class, "status": status})
        if lineage in {"high", "unknown"}:
            warnings.append({"type": "source_lineage_risk", "source_class": source_class, "status": lineage})
        if independence in {"dependent", "unknown"}:
            warnings.append({"type": "independence_not_established", "source_class": source_class, "status": independence})

    return {
        "ok": not errors,
        "path": str(path),
        "required_classes": list(required_classes),
        "results": results,
        "errors": errors,
        "warnings": warnings,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check source portfolio coverage.")
    parser.add_argument("portfolio_file", type=Path)
    parser.add_argument("--required", default=",".join(DEFAULT_REQUIRED_CLASSES))
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    required = tuple(item.strip() for item in args.required.split(",") if item.strip())
    result = check(args.portfolio_file, required)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(("PASS" if result["ok"] else "FAIL") + f": {args.portfolio_file}")
        for error in result["errors"]:
            print(f"- error: {error['type']} {error.get('source_class', '')} {error.get('status', '')}".rstrip())
        for warning in result["warnings"]:
            print(f"- warning: {warning['type']} {warning.get('source_class', '')} {warning.get('status', '')}".rstrip())
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
