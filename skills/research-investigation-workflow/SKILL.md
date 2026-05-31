---
name: research-investigation-workflow
description: Coordinate multi-round research and investigation work with existing Guard-family workflows. Use when Codex must investigate a topic, collect or triage evidence, reconstruct timelines or storylines, separate findings from hypotheses, synthesize a research report, audit claims, track stale evidence, or record reusable investigation history with TraceGuard, LogicGuard, FlowGuard, and a Research Investigation History Ledger.
---

# Research Investigation Workflow

Use this skill to run an evidence-led investigation from user goal intake to final report and reusable run history. Build a thin orchestration layer over existing TraceGuard, LogicGuard, and FlowGuard workflows; do not create a new reasoning engine.

## Core Boundaries

- Keep TraceGuard Case Library for messy case evidence, directions, events, traces, gaps, and contradictions.
- Keep LogicGuard Source Library for durable formal source support and argument models.
- Keep FlowGuard logs and models for process evidence, stale-check review, and closure confidence.
- Keep Research Investigation History Ledger for run-level workflow memory and artifact pointers.
- Do not merge TraceGuard Case Library with LogicGuard Source Library.
- Do not treat History Ledger records, saved sources, confidence scores, or hypotheses as factual proof.
- Do not write confident prose from missing, stale, permission-gated, or contradicted evidence.

## Required Start

1. Read `references/workflow.md` and `references/history-ledger.md`.
2. Search the Research Investigation History Ledger before new evidence work.
3. Classify the evidence-source policy: public, local, internal, permission-gated, and hypothesis/inference.
4. Check current TraceGuard, LogicGuard, and FlowGuard command surfaces before claiming a concrete command path is valid.
5. Use FlowGuard for multi-stage freshness and closure when the investigation has more than a short single-pass answer.

## Route

Use TraceGuard when the task involves messy evidence, timelines, event reconstruction, contradictions, gap ledgers, or safe/unsafe claim boundaries. Load `references/traceguard-loop.md`.

Use LogicGuard when stable sources should be preserved, claims need support modeling, report structure is needed, or final prose must be audited. Load `references/logicguard-report-synthesis.md`.

Use FlowGuard when stage order, changed artifacts, stale evidence, skipped checks, revalidation, or completion claims matter. Load `references/flowguard-closure.md`.

Use `references/evidence-source-policy.md` before searching or using non-public material. Use `references/output-contract.md` before final delivery.

## Investigation Loop

Run the investigation as:

```text
history preflight -> goal intake -> evidence policy -> search/save sources -> TraceGuard model -> gap-driven search loop -> explicit source promotion -> LogicGuard model/deepen/synthesize -> LogicGuard final claim audit -> FlowGuard closure -> final delivery -> history postflight
```

Continue the loop until the requested conclusion strength is supported, the budget is reached, critical evidence is inaccessible, remaining gaps are accepted, or claims are downgraded to match evidence.

## Final Delivery

Deliver a readable main report first, then appendix material. Include findings, confidence/evidence levels, timeline or storyline, hypotheses, assumptions, unresolved gaps, source appendix, TraceGuard summary, LogicGuard audit summary, FlowGuard closure summary, and History Ledger postflight status as appropriate.

If closure is partial or blocked, say exactly what is missing and which claim strength remains supported.
