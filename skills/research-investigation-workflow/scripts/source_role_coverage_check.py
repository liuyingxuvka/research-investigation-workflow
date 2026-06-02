#!/usr/bin/env python
"""Check source-role coverage records for research investigations."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


DEFAULT_REQUIRED_ROLES = (
    "claim_origin",
    "direct_or_original_facts",
    "source_statements",
    "scope_boundaries",
    "execution_or_outcome_evidence",
    "counter_or_limiting_evidence",
    "future_trigger_conditions",
)

PASS_VALUES = {"found", "read", "anchored", "complete", "covered", "not_applicable", "not-applicable"}
BLOCK_VALUES = {"gap", "blocked", "access_gap", "access-gap", "not_run", "not-run", "missing", "unknown"}


def load_data(path: Path) -> Any:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        return json.loads(text)
    try:
        import yaml  # type: ignore
    except Exception as exc:  # pragma: no cover - environment-dependent
        raise SystemExit(f"YAML input requires PyYAML: {exc}") from exc
    return yaml.safe_load(text)


def find_coverage(data: Any) -> dict[str, Any]:
    if isinstance(data, dict):
        if "source_role_coverage" in data and isinstance(data["source_role_coverage"], dict):
            return data["source_role_coverage"]
        for key in ("sourceguard", "source_guard", "coverage"):
            nested = data.get(key)
            if isinstance(nested, dict) and isinstance(nested.get("source_role_coverage"), dict):
                return nested["source_role_coverage"]
    raise SystemExit("No source_role_coverage mapping found.")


def normalize(value: Any) -> str:
    if isinstance(value, dict):
        for key in ("status", "state", "coverage"):
            if key in value:
                return str(value[key]).strip().lower().replace(" ", "_")
        return "unknown"
    return str(value).strip().lower().replace(" ", "_")


def check_coverage(path: Path, required_roles: tuple[str, ...]) -> dict[str, Any]:
    coverage = find_coverage(load_data(path))
    role_results = []
    errors = []
    warnings = []
    for role in required_roles:
        status = normalize(coverage.get(role, "missing"))
        passed = status in PASS_VALUES
        blocked = status in BLOCK_VALUES or not passed
        item = {"role": role, "status": status, "passed": passed}
        role_results.append(item)
        if blocked:
            errors.append({"type": "required_role_not_covered", "role": role, "status": status})

    for role, value in coverage.items():
        status = normalize(value)
        if status in BLOCK_VALUES and role not in required_roles:
            warnings.append({"type": "optional_role_gap", "role": role, "status": status})

    return {
        "ok": not errors,
        "path": str(path),
        "required_roles": list(required_roles),
        "roles": role_results,
        "errors": errors,
        "warnings": warnings,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check source-role coverage status.")
    parser.add_argument("coverage_file", type=Path)
    parser.add_argument("--required", default=",".join(DEFAULT_REQUIRED_ROLES))
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    required = tuple(role.strip() for role in args.required.split(",") if role.strip())
    result = check_coverage(args.coverage_file, required)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        status = "PASS" if result["ok"] else "FAIL"
        print(f"{status}: {args.coverage_file}")
        for error in result["errors"]:
            print(f"- error: {error['role']} is {error['status']}")
        for warning in result["warnings"]:
            print(f"- warning: {warning['role']} is {warning['status']}")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
