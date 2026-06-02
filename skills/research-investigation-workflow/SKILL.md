---
name: research-investigation-workflow
description: Coordinate heavy multi-round research and investigation work with existing Guard-family workflows. Use when Codex must investigate a topic, build a generic Research Reasoning Atlas, expand logic branches, map pro/con and alternative explanations, select analytical model lenses, map expert stances, plan public/local/internal evidence discovery with SourceGuard, reconstruct competing timelines or storylines with TraceGuard, synthesize a research-backed final artifact such as a report, paper, memo, brief, article, or deck storyline, audit claims with LogicGuard, track stale evidence, or record reusable investigation history.
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
- Do not hard-code domain-specific checklists into this core skill. Use generic reasoning categories in the main workflow, and treat topic-specific details as selected model lenses, examples, or future domain packs.
- Do not reward branch volume by itself. Branches matter only when they affect conclusion strength, scope, method, evidence needs, or reader decisions.
- Keep a source registry for every substantive final artifact. A source listed in the appendix must have a source id, role, date or freshness clue when known, locator or access note, and the important claims it supports or limits.
- Do not let final citations drift away from the source registry. Every important inline marker must resolve to one registered source, and every important registered source must have a visible role or an explicit reason it is appendix-only.
- Keep a source portfolio plan for substantive investigations. Important source classes should be explicitly considered: primary or closest-available records, official/regulatory records when relevant, execution or outcome records, independent or third-party records, expert/model sources when interpretation matters, counter or limiting sources, source-lineage checks, and future-trigger sources. Missing high-value classes must become SourceGuard search actions, access gaps, or claim downgrades.
- Keep a key-claim and key-number ledger for material figures, quantified claims, and central conclusions. Each entry should name the source id, source role, date or coverage period, claim type, what the source can support, what it cannot support, unsafe overclaim wording, allowed wording, final treatment, and required citation marker.
- For causal, price, market, policy, adoption, execution, outcome, or impact claims, keep an explicit transmission/effect chain. Separate cause, mechanism, intermediate signal, outcome, stakeholder signal, counter or limiting evidence, and future trigger before writing strong final wording.
- Use TraceGuard and LogicGuard deeply, not just as final coarse gates. TraceGuard should preserve lead-level, event/explanation/outcome-layer, execution-chain, competing-storyline, causal, counterfactual, and confounder state. LogicGuard should model the requested artifact at its natural hierarchy: document/section/paragraph, deck/section/slide, paper/section/paragraph, memo/decision block, or another user-requested structure.
- Final artifact review must be genre-adaptive. Check whether the output fits the user's requested artifact type, audience, and delivery profile; do not impose a fixed report style when the user asked for a paper, memo, article, deck storyline, decision note, or another form.
- Keep generated investigation outputs local-only by default. Do not commit reports, TraceGuard cases, LogicGuard source libraries, or History Ledger records to the skill/software repository unless the user explicitly asks for a sanitized published sample.

## Required Start

1. Read `references/workflow.md`, `references/reasoning-atlas.md`, `references/sourceguard-discovery-loop.md`, and `references/history-ledger.md`.
2. Search the Research Investigation History Ledger before new evidence work.
3. Classify the evidence-source policy: public, local, internal, permission-gated, and hypothesis/inference.
4. Build an initial logic-lead map before broad writing: actors, motives, event facts, outcomes, contradictions, limiting evidence, follow-up consequences, and alternative explanations.
5. Build a general evidence-role map before writing: claim or rumor origin, direct/original facts, source statements, scope boundaries, execution or outcome evidence, context or motive evidence, expert interpretation, counter/limiting evidence, and future trigger conditions. Do not collapse these roles into one storyline.
6. Build a generic Research Reasoning Atlas before broad search or final writing: branch tree, debate matrix, alternative explanations, confounders, selected analytical lenses, expert stance map when relevant, counterfactual needs, and conclusion-tournament candidates.
7. Start a source registry before broad search. Add candidate source ids as soon as material is found, then update each record with role, locator, access status, source date, coverage period, and claim use as the investigation matures.
8. Build a source portfolio plan and key-claim/key-number ledger before broad drafting. Keep them lightweight but explicit enough to show high-value source gaps, numeric provenance, support boundaries, and unsafe wording.
9. Build or update a SourceGuard belief state before broad search. Let SourceGuard rank the next public/local/internal search actions and record permission-gated material as access gaps.
10. For substantive final artifacts, run the minimum investigation rounds: original-fact round, counter/limiting round, impact/execution round, stakeholder round, and future-trigger round. If a round cannot be completed, downgrade the closure and claim strength.
11. Check current SourceGuard, TraceGuard, LogicGuard, and FlowGuard command surfaces before claiming a concrete command path is valid.
12. Use FlowGuard for multi-stage freshness and closure when the investigation has more than a short single-pass answer.

## Route

Use SourceGuard when the task needs source discovery, branch-aware evidence search planning, local/internal/public source triage, counter/limiting or disconfirming source search, source-lineage review, expert/model source discovery, multimodal anchor planning, permission/access-gap tracking, source-role coverage review, or post-draft source-gap planning. Load `references/sourceguard-discovery-loop.md`. SourceGuard ranks search value; it does not validate facts, traces, citations, or final claims.

Use TraceGuard when the task involves messy evidence, timelines, event reconstruction, logic leads, explanation candidates, competing storylines, causal chains, counterfactual traces, confounder ledgers, contradictions, gap ledgers, announcement-to-execution chains, or safe/unsafe claim boundaries. Load `references/traceguard-loop.md`.

Use LogicGuard when stable sources should be preserved, claims need support modeling, target artifact structure is needed, inline citations must be assigned, citation markers must be checked against the source registry, model lenses must become warrants, expert stances must be typed, conclusion tournaments must be judged, or final prose must be audited. Load `references/logicguard-report-synthesis.md`.

Use FlowGuard when stage order, changed artifacts, stale evidence, skipped checks, revalidation, local-output privacy, or completion claims matter. Load `references/flowguard-closure.md`. Do not change FlowGuard itself for report-writing rules; encode research-specific closure rules in this skill.

Use `references/evidence-source-policy.md` before searching or using non-public material. Use `references/output-contract.md` before final delivery.

## Investigation Loop

Run the investigation as:

```text
history preflight -> goal intake -> research plan card -> evidence policy -> logic-lead map -> evidence-role map -> Research Reasoning Atlas -> source registry -> source portfolio plan -> key-claim/key-number ledger -> SourceGuard branch-aware search plan -> execute allowed searches -> SourceGuard observations/update -> source-role and portfolio coverage check -> per-round replan gate -> TraceGuard layered lead / competing storyline / causal / counterfactual / execution-chain / effect-chain model -> SourceGuard gap-driven re-search loop -> explicit source promotion -> LogicGuard hierarchical claim-to-source matrix and conclusion tournament -> genre-adaptive section/paragraph/slide/artifact blueprint -> citation-grounded final artifact -> citation registry and semantic source-fit audit -> LogicGuard final claim audit -> final research quality gate -> reader-facing artifact cleanup -> FlowGuard closure -> final delivery -> history postflight
```

Continue the loop until the requested conclusion strength is supported, the budget is reached, critical evidence is inaccessible, remaining gaps are accepted, or claims are downgraded to match evidence.

## Final Delivery

Deliver a readable final artifact in the genre the user requested, then appendix or support material when useful. The final artifact may be a report, paper, memo, brief, article, literature review, deck storyline, decision note, or another research-backed artifact. Long artifacts need a brief reader route near the start so the reader knows which question is answered first, why sections follow in that order, and where limitations appear. The reader-facing artifact must not expose internal Guard-family terms such as `SourceGuard`, `TraceGuard`, `LogicGuard`, `FlowGuard`, or `History Ledger` unless the user explicitly asks for a methods appendix. Use ordinary language instead: source search plan, event chain, evidence chain, argument structure, process check, and run notes. Keep internal workflow summaries in the appendix or local run record.

The final artifact must include inline citation markers for important claims and make source roles visible when ambiguity matters: event fact, source claim, independent report, limiting evidence, expert analysis, historical background, hypothesis, or forecast. Coverage obligations may appear as natural prose, citations, footnotes, tables, or appendix depending on the requested genre. Do not force source-role categories into visible headings unless that improves the requested artifact. Include findings, confidence/evidence levels, timeline or storyline, logic-lead coverage, Atlas-derived debate outcomes, hypotheses, assumptions, unresolved gaps, source registry or source appendix, and appendix-level Guard-family summaries as appropriate.

For Markdown final artifacts that use compact `[S#]` source markers, run the citation-marker helper when available before final delivery:

```powershell
python %USERPROFILE%\\.codex\\skills\research-investigation-workflow\scripts\audit_markdown_sources.py <artifact.md> --json
```

If the helper reports undefined citation markers, duplicate source ids, or another hard error, repair the artifact or downgrade closure. Warnings such as unused source entries may remain only when they are explicitly appendix-only, method-only, or background-only.

For source-role coverage ledgers written as JSON or YAML, run the coverage helper when available before claiming a complete or deep investigation:

```powershell
python %USERPROFILE%\\.codex\\skills\research-investigation-workflow\scripts\source_role_coverage_check.py <coverage.json-or-yaml> --json
```

If required roles are missing, not run, or gap-labeled, return to SourceGuard for targeted discovery or downgrade the claim strength.

When source portfolio, key-claim, or semantic-fit ledgers exist, run the corresponding helpers when available:

```powershell
python %USERPROFILE%\\.codex\\skills\research-investigation-workflow\scripts\source_portfolio_check.py <portfolio.json-or-yaml> --json
python %USERPROFILE%\\.codex\\skills\research-investigation-workflow\scripts\key_claim_ledger_check.py <ledger.json-or-yaml> --json
python %USERPROFILE%\\.codex\\skills\research-investigation-workflow\scripts\claim_support_fit_check.py <fit-ledger.json-or-yaml> --json
```

Helper checks catch structural gaps only. LogicGuard still owns exact semantic review of whether a cited source supports the final wording, scope, tense, causality, execution, outcome, price layer, or forecast claim.

For negative or partial findings, name the missing evidence roles or concrete signals that were checked or not found. Examples: direct primary record, scope-defining document, implementation or execution record, outcome data, affected-stakeholder evidence, limiting source, or observable future trigger.

If the fact, counter/limiting, impact/execution, stakeholder, or future-trigger rounds were not completed, do not label the output a complete investigation or conclusive artifact. Deliver an initial investigation, staged artifact, qualified finding, or downgraded conclusion that matches the evidence.

Before final delivery, run or simulate a final research quality gate:

- Source registry complete enough for the artifact's important claims.
- Source portfolio complete enough for the artifact's claim strength, or missing high-value source classes named and downgraded.
- Key-claim/key-number ledger covers material figures and central conclusions with support boundaries and unsafe wording.
- Research Reasoning Atlas complete enough for central claims: branch tree, strongest opposition, alternatives, selected lenses, expert stances when relevant, and conclusion tournament status.
- TraceGuard has modeled important leads at the needed depth: event fact, explanation, outcome or impact, execution chain, competing storyline, causal chain, counterfactual, confounder, and safe wording.
- Source-role coverage checked and unresolved gaps named.
- Announcement, implementation, execution, outcome, stakeholder, and future-trigger chains separated where relevant.
- LogicGuard has modeled important artifact units at the requested genre's natural hierarchy, and the claim-to-source matrix, inline citation markers, and semantic source-fit checks agree.
- Reader-facing prose follows the user's requested artifact type and does not hide material limitations or leak internal workflow terms unless requested.
- Closure status matches the weakest important unresolved evidence role, stale check, or citation audit result.

If closure is partial or blocked, say exactly what is missing and which claim strength remains supported.
