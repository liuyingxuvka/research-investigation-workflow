---
name: research-investigation-workflow
description: Coordinate heavy multi-round research and investigation work with existing Guard-family workflows. Use when Codex must investigate a topic, plan public/local/internal evidence discovery with SourceGuard, collect or triage sources, reconstruct timelines or storylines, separate findings from hypotheses, synthesize a research-backed final artifact such as a report, paper, memo, brief, article, or deck storyline, audit claims, track stale evidence, or record reusable investigation history with SourceGuard, TraceGuard, LogicGuard, FlowGuard, and a Research Investigation History Ledger.
---

# Research Investigation Workflow

Use this skill to run a deep, evidence-led investigation from user goal intake to a research-backed final artifact and reusable run history. Build a thin orchestration layer over existing SourceGuard, TraceGuard, LogicGuard, and FlowGuard workflows; do not create a new reasoning engine.

## Core Boundaries

- Keep TraceGuard Case Library for messy case evidence, directions, events, traces, gaps, and contradictions.
- Keep SourceGuard for source-discovery planning, candidate source records, evidence-anchor needs, access gaps, and next-search action ranking.
- Keep LogicGuard Source Library for durable formal source support and argument models.
- Keep FlowGuard logs and models for process evidence, stale-check review, and closure confidence.
- Keep Research Investigation History Ledger for run-level workflow memory and artifact pointers.
- Do not merge TraceGuard Case Library with LogicGuard Source Library.
- Do not treat History Ledger records, saved sources, confidence scores, or hypotheses as factual proof.
- Do not treat SourceGuard utility scores, source candidates, search hits, or planned search actions as factual proof.
- Do not write confident prose from missing, stale, permission-gated, or contradicted evidence.
- Do not measure investigation depth by source counts or shallow/medium/deep modes. Measure depth by whether important logic leads and evidence chains have been pursued, limited, contradicted, or explicitly downgraded.
- Keep generated investigation outputs local-only by default. Do not commit reports, TraceGuard cases, LogicGuard source libraries, or History Ledger records to the skill/software repository unless the user explicitly asks for a sanitized published sample.

## Required Start

1. Read `references/workflow.md`, `references/sourceguard-discovery-loop.md`, and `references/history-ledger.md`.
2. Search the Research Investigation History Ledger before new evidence work.
3. Classify the evidence-source policy: public, local, internal, permission-gated, and hypothesis/inference.
4. Build an initial logic-lead map before broad writing: actors, motives, event facts, outcomes, contradictions, limiting evidence, follow-up consequences, and alternative explanations.
5. Build a general evidence-role map before writing: claim or rumor origin, direct/original facts, source statements, scope boundaries, execution or outcome evidence, context or motive evidence, expert interpretation, counter/limiting evidence, and future trigger conditions. Do not collapse these roles into one storyline.
6. Build or update a SourceGuard belief state before broad search. Let SourceGuard rank the next public/local/internal search actions and record permission-gated material as access gaps.
7. For substantive final artifacts, run the minimum investigation rounds: original-fact round, counter/limiting round, impact/execution round, stakeholder round, and future-trigger round. If a round cannot be completed, downgrade the closure and claim strength.
8. Check current SourceGuard, TraceGuard, LogicGuard, and FlowGuard command surfaces before claiming a concrete command path is valid.
9. Use FlowGuard for multi-stage freshness and closure when the investigation has more than a short single-pass answer.

## Route

Use SourceGuard when the task needs source discovery, evidence search planning, local/internal/public source triage, counter/limiting source search, multimodal anchor planning, or permission/access-gap tracking. Load `references/sourceguard-discovery-loop.md`. SourceGuard ranks search value; it does not validate facts, traces, or final claims.

Use TraceGuard when the task involves messy evidence, timelines, event reconstruction, logic leads, explanation candidates, contradictions, gap ledgers, or safe/unsafe claim boundaries. Load `references/traceguard-loop.md`.

Use LogicGuard when stable sources should be preserved, claims need support modeling, target artifact structure is needed, inline citations must be assigned, or final prose must be audited. Load `references/logicguard-report-synthesis.md`.

Use FlowGuard when stage order, changed artifacts, stale evidence, skipped checks, revalidation, local-output privacy, or completion claims matter. Load `references/flowguard-closure.md`. Do not change FlowGuard itself for report-writing rules; encode research-specific closure rules in this skill.

Use `references/evidence-source-policy.md` before searching or using non-public material. Use `references/output-contract.md` before final delivery.

## Investigation Loop

Run the investigation as:

```text
history preflight -> goal intake -> research plan card -> evidence policy -> logic-lead map -> evidence-role map -> SourceGuard belief state -> SourceGuard-ranked search plan -> execute allowed searches -> SourceGuard observations/update -> per-round replan gate -> TraceGuard lead/event/evidence-chain model -> SourceGuard gap-driven re-search loop -> explicit source promotion -> LogicGuard claim-to-source matrix -> section/paragraph/artifact blueprint -> citation-grounded final artifact -> LogicGuard final claim audit -> reader-facing artifact cleanup -> FlowGuard closure -> final delivery -> history postflight
```

Continue the loop until the requested conclusion strength is supported, the budget is reached, critical evidence is inaccessible, remaining gaps are accepted, or claims are downgraded to match evidence.

## Final Delivery

Deliver a readable final artifact in the genre the user requested, then appendix or support material when useful. The final artifact may be a report, paper, memo, brief, article, literature review, deck storyline, decision note, or another research-backed artifact. Long artifacts need a brief reader route near the start so the reader knows which question is answered first, why sections follow in that order, and where limitations appear. The reader-facing artifact must not expose internal Guard-family terms such as `SourceGuard`, `TraceGuard`, `LogicGuard`, `FlowGuard`, or `History Ledger` unless the user explicitly asks for a methods appendix. Use ordinary language instead: source search plan, event chain, evidence chain, argument structure, process check, and run notes. Keep internal workflow summaries in the appendix or local run record.

The final artifact must include inline citation markers for important claims and make source roles visible when ambiguity matters: event fact, source claim, independent report, limiting evidence, expert analysis, historical background, hypothesis, or forecast. Coverage obligations may appear as natural prose, citations, footnotes, tables, or appendix depending on the requested genre. Do not force source-role categories into visible headings unless that improves the requested artifact. Include findings, confidence/evidence levels, timeline or storyline, logic-lead coverage, hypotheses, assumptions, unresolved gaps, source appendix, and appendix-level Guard-family summaries as appropriate.

For negative or partial findings, name the missing evidence roles or concrete signals that were checked or not found. Examples: direct primary record, scope-defining document, implementation or execution record, outcome data, affected-stakeholder evidence, limiting source, or observable future trigger.

If the fact, counter/limiting, impact/execution, stakeholder, or future-trigger rounds were not completed, do not label the output a complete investigation or conclusive artifact. Deliver an initial investigation, staged artifact, qualified finding, or downgraded conclusion that matches the evidence.

If closure is partial or blocked, say exactly what is missing and which claim strength remains supported.
