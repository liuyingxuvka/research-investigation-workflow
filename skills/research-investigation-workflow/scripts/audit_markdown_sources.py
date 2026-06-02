#!/usr/bin/env python
"""Audit simple Markdown source markers for research artifacts.

This helper checks deterministic marker hygiene only. It does not decide
whether a source semantically supports a claim; LogicGuard still owns the
claim-to-source audit.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


SOURCE_DEF_RE = re.compile(r"^\s*\[(S\d+)\]\s+(.+)$", re.MULTILINE)
SOURCE_REF_RE = re.compile(r"\[(S\d+(?:\s*[;,，、]\s*S\d+)*(?:\s*,\s*[^\]]+)?)\]")
SOURCE_ID_RE = re.compile(r"\bS\d+\b")


def split_body_and_sources(text: str) -> tuple[str, str]:
    match = re.search(r"^##\s+(来源列表|Sources|Source List|References)\s*$", text, re.MULTILINE)
    if not match:
        return text, ""
    return text[: match.start()], text[match.start() :]


def collect_refs(text: str) -> set[str]:
    refs: set[str] = set()
    for marker in SOURCE_REF_RE.findall(text):
        refs.update(SOURCE_ID_RE.findall(marker))
    return refs


def audit_markdown(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    body, sources = split_body_and_sources(text)
    source_defs = {source_id: body.strip() for source_id, body in SOURCE_DEF_RE.findall(sources)}
    body_refs = collect_refs(body)
    non_definition_source_lines = "\n".join(
        line for line in sources.splitlines() if not SOURCE_DEF_RE.match(line)
    )
    source_section_refs = collect_refs(non_definition_source_lines)

    undefined_refs = sorted(body_refs - set(source_defs), key=lambda s: int(s[1:]))
    unused_defs = sorted(set(source_defs) - body_refs, key=lambda s: int(s[1:]))
    duplicate_defs = sorted(
        source_id
        for source_id in set(source_id for source_id, _ in SOURCE_DEF_RE.findall(sources))
        if [sid for sid, _ in SOURCE_DEF_RE.findall(sources)].count(source_id) > 1
    )
    grouped_defs = sorted(
        source_id
        for source_id, definition in source_defs.items()
        if definition.count("http://") + definition.count("https://") > 1
    )

    findings: list[dict[str, str]] = []
    for source_id in undefined_refs:
        findings.append({"severity": "error", "type": "undefined_reference", "source_id": source_id})
    for source_id in duplicate_defs:
        findings.append({"severity": "error", "type": "duplicate_definition", "source_id": source_id})
    for source_id in unused_defs:
        findings.append({"severity": "warning", "type": "unused_definition", "source_id": source_id})
    for source_id in grouped_defs:
        findings.append({"severity": "warning", "type": "multi_url_definition", "source_id": source_id})
    if source_section_refs:
        findings.append({
            "severity": "warning",
            "type": "source_section_contains_inline_marker",
            "source_id": ",".join(sorted(source_section_refs, key=lambda s: int(s[1:]))),
        })

    return {
        "ok": not any(f["severity"] == "error" for f in findings),
        "path": str(path),
        "body_ref_count": len(body_refs),
        "source_definition_count": len(source_defs),
        "undefined_refs": undefined_refs,
        "unused_defs": unused_defs,
        "duplicate_defs": duplicate_defs,
        "multi_url_defs": grouped_defs,
        "findings": findings,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Audit Markdown [S#] source markers.")
    parser.add_argument("markdown", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    result = audit_markdown(args.markdown)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        status = "PASS" if result["ok"] else "FAIL"
        print(f"{status}: {args.markdown}")
        for finding in result["findings"]:
            print(f"- {finding['severity']}: {finding['type']} {finding.get('source_id', '')}".rstrip())
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
