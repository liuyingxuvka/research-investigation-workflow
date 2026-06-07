#!/usr/bin/env python
"""Aggregate research investigation helper checks into one closure report."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
from typing import Any, Callable


SCRIPT_DIR = Path(__file__).resolve().parent


def _load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"Cannot load helper: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _load_json(path: Path | None) -> dict[str, Any]:
    if path is None:
        return {}
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise SystemExit(f"{path} must contain a JSON object")
    return value


def _add_check(
    findings: list[dict[str, Any]],
    checked_inputs: list[dict[str, str]],
    label: str,
    path: Path | None,
    func: Callable[[Path], dict[str, Any]],
) -> None:
    if path is None:
        findings.append({
            "severity": "warning",
            "type": "optional_check_not_run",
            "check": label,
            "message": f"{label} input was not provided.",
        })
        return
    checked_inputs.append({"check": label, "path": str(path)})
    result = func(path)
    for item in result.get("findings", []):
        findings.append({"check": label, **item})
    for item in result.get("errors", []):
        findings.append({"severity": "error", "check": label, **item})
    for item in result.get("warnings", []):
        findings.append({"severity": "warning", "check": label, **item})
    if not result.get("ok", False):
        findings.append({
            "severity": "error",
            "type": "helper_failed",
            "check": label,
            "message": f"{label} helper reported a failing result.",
        })


def _status(findings: list[dict[str, Any]], ledger: dict[str, Any]) -> str:
    if any(str(item.get("severity", "")).lower() in {"error", "blocker"} for item in findings):
        return "blocked"
    declared = str(ledger.get("closure_status", "")).lower()
    if declared in {"passed", "partial", "blocked", "downgraded"}:
        return declared
    if findings:
        return "partial"
    return "passed"


def check(args: argparse.Namespace) -> dict[str, Any]:
    ledger = _load_json(args.ledger)
    findings: list[dict[str, Any]] = []
    checked_inputs: list[dict[str, str]] = []
    missing_inputs: list[dict[str, str]] = []
    stale_evidence: list[dict[str, str]] = []
    skipped_checks: list[dict[str, str]] = []

    audit_markdown = _load_module("audit_markdown_sources", SCRIPT_DIR / "audit_markdown_sources.py")
    source_roles = _load_module("source_role_coverage_check", SCRIPT_DIR / "source_role_coverage_check.py")
    portfolio = _load_module("source_portfolio_check", SCRIPT_DIR / "source_portfolio_check.py")
    key_claim = _load_module("key_claim_ledger_check", SCRIPT_DIR / "key_claim_ledger_check.py")
    fit = _load_module("claim_support_fit_check", SCRIPT_DIR / "claim_support_fit_check.py")

    _add_check(findings, checked_inputs, "markdown_sources", args.artifact, audit_markdown.audit_markdown)
    _add_check(findings, checked_inputs, "source_role_coverage", args.coverage, lambda p: source_roles.check_coverage(p, source_roles.DEFAULT_REQUIRED_ROLES))
    _add_check(findings, checked_inputs, "source_portfolio", args.portfolio, lambda p: portfolio.check(p, portfolio.DEFAULT_REQUIRED_CLASSES))
    _add_check(findings, checked_inputs, "key_claim_ledger", args.key_claim_ledger, key_claim.check)
    _add_check(findings, checked_inputs, "claim_support_fit", args.fit_ledger, fit.check)

    for required in ("source_registry_status", "traceguard_status", "logicguard_status", "final_artifact_status"):
        if not ledger.get(required):
            missing_inputs.append({"field": required, "message": f"Research ledger is missing {required}."})

    if str(ledger.get("final_artifact_status", "")).lower() in {"stale_after_edit", "draft_after_audit"}:
        stale_evidence.append({
            "field": "final_artifact_status",
            "message": "Final artifact changed after audit; rerun citation/source-fit/LogicGuard checks.",
        })

    for item in ledger.get("skipped_checks", []) if isinstance(ledger.get("skipped_checks"), list) else []:
        skipped_checks.append({"check": str(item), "message": "Research ledger records a skipped check."})

    if missing_inputs:
        findings.append({"severity": "warning", "type": "ledger_missing_required_fields", "count": len(missing_inputs)})
    if stale_evidence:
        findings.append({"severity": "error", "type": "stale_research_evidence", "count": len(stale_evidence)})
    if skipped_checks:
        findings.append({"severity": "warning", "type": "skipped_research_checks", "count": len(skipped_checks)})

    closure_status = _status(findings, ledger)
    next_actions = []
    if findings or missing_inputs or stale_evidence or skipped_checks:
        next_actions.append({
            "owner": "research-investigation-workflow",
            "action": "repair_or_downgrade_from_closure_findings",
            "reason": "Research closure found missing, stale, skipped, or failing checks.",
        })
    if any(item.get("check") in {"source_role_coverage", "source_portfolio", "key_claim_ledger", "claim_support_fit"} and item.get("severity") == "error" for item in findings):
        next_actions.append({"owner": "sourceguard", "action": "targeted_source_research_or_claim_downgrade"})
    if stale_evidence:
        next_actions.append({"owner": "flowguard", "action": "rerun_stale_evidence_gate"})

    return {
        "owner_guard": "research-investigation-workflow",
        "artifact_kind": "research_investigation_closure",
        "closure_status": closure_status,
        "checked_inputs": checked_inputs,
        "findings": findings,
        "missing_inputs": missing_inputs,
        "stale_evidence": stale_evidence,
        "skipped_checks": skipped_checks,
        "next_actions": next_actions,
        "safe_claim": ledger.get("safe_claim", "Research output is only as strong as the weakest current evidence role."),
        "unsafe_claim_boundary": ledger.get("unsafe_claim_boundary", "Do not call the investigation complete while helper errors, stale evidence, or required ledgers remain unresolved."),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run research investigation closure checks.")
    parser.add_argument("--ledger", type=Path)
    parser.add_argument("--artifact", type=Path, help="Markdown artifact with [S#] source markers.")
    parser.add_argument("--coverage", type=Path, help="Source-role coverage JSON/YAML.")
    parser.add_argument("--portfolio", type=Path, help="Source portfolio JSON/YAML.")
    parser.add_argument("--key-claim-ledger", type=Path)
    parser.add_argument("--fit-ledger", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    result = check(args)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"{result['closure_status'].upper()}: research investigation closure")
        for finding in result["findings"]:
            print(f"- {finding.get('severity', 'warning')}: {finding.get('type', '')} {finding.get('check', '')}".rstrip())
    return 0 if result["closure_status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
