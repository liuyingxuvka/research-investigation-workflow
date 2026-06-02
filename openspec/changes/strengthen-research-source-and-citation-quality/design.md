## Context

`research-investigation-workflow` already orchestrates SourceGuard, TraceGuard, LogicGuard, and run history for deep investigations. The current contracts separate source discovery, evidence/storyline reconstruction, and final argument audit, but real report comparison exposed three practical gaps:

- high-value source classes can be missed after an apparently strong first pass;
- announcements, forecasts, contracts, execution, and outcomes need a more explicit chain;
- final Markdown reports can contain citation/source-id mismatches that are not caught by prose-level claim audit.

The upgrade must preserve the existing thin orchestration design. It must not create a new reasoning engine or blur SourceGuard, TraceGuard, and LogicGuard ownership.

## Goals / Non-Goals

**Goals:**

- Add a source registry that follows a source from discovery to final citation.
- Make SourceGuard responsible for source-role coverage review and post-draft source-gap review.
- Make TraceGuard responsible for announcement-to-execution chain status and safe wording handoff.
- Make LogicGuard responsible for final citation consistency, claim-to-source coverage, and source-role misuse audit.
- Make the research workflow enforce these checks before marking a substantive artifact complete.
- Add small deterministic helpers for Markdown citation/source consistency and source-role coverage.
- Sync source skill files and installed skill files after edits.

**Non-Goals:**

- Do not add a crawler, browser automation loop, UI, dashboard, or standalone app.
- Do not make SourceGuard decide factual truth.
- Do not make TraceGuard write final conclusions.
- Do not make LogicGuard store messy investigation evidence.
- Do not upgrade FlowGuard's skill behavior as part of this change; FlowGuard is used only for process/order validation evidence.
- Do not force final artifacts to expose internal Guard-family names or diagnostic tables when the requested genre would be harmed.

## Decisions

1. **Use a source registry as the handoff spine.**
   Rationale: Citation mismatches usually happen when source ids are recreated during drafting. A registry keeps `S#`, title, publisher, date, URL, source role, support boundary, and claim use in one inspectable record. Alternative considered: rely on the existing bibliography only. Rejected because a final bibliography cannot verify paragraph-level source use.

2. **Make source-role coverage a required SourceGuard output.**
   Rationale: SourceGuard already owns leads, gaps, actions, observations, and handoff readiness. It is the natural place to say whether primary, independent, counter, execution/outcome, stakeholder, freshness, and future-trigger source roles are found, read, anchored, blocked, or still missing. Alternative considered: leave this to the final writer. Rejected because the writer is too late in the loop to discover systematic source gaps cheaply.

3. **Make execution-chain status a required TraceGuard handoff for substantive leads.**
   Rationale: Research artifacts often overclaim by jumping from announcement to execution or outcome. TraceGuard already owns event/evidence/storyline boundaries, so it should label each important lead as announcement, approval, contract, construction, operation, market result, outcome, or unresolved. Alternative considered: put this only in LogicGuard. Rejected because LogicGuard audits the written claim, while the evidence-chain boundary should be visible before drafting.

4. **Make LogicGuard citation audit mandatory before final delivery.**
   Rationale: LogicGuard already owns citation matrices and final claim support. It should treat undefined markers, unused source definitions, source-role mismatch, generated markers, and stale audit after prose edits as blocking or downgrade-worthy evidence. Alternative considered: only ask the agent to be careful. Rejected because citation id errors are deterministic enough to check.

5. **Add lightweight scripts before schema-heavy model changes.**
   Rationale: Current CLI models already support enough structure for this upgrade through skill contracts and report artifacts. Small scripts can catch the highest-risk Markdown citation failures without requiring new Guard package releases. If future regressions show the contracts are too soft, a later change can add first-class model fields.

## Risks / Trade-offs

- **Risk: More gates slow small answers** → Apply the full gate only to substantive source-backed investigation artifacts; keep quick answers downgraded as initial leads or working hypotheses.
- **Risk: Final reports become checklist-like** → Keep matrices and audit results in appendix or run notes unless the requested artifact benefits from visible tables.
- **Risk: Citation audit catches marker presence but not semantic support** → Combine deterministic marker checks with LogicGuard claim-to-source matrix review and source-role wording checks.
- **Risk: Source registry becomes stale after edits** → Require final audit after the last material prose edit; if prose changes afterward, mark audit stale and rerun.
- **Risk: Multiple agents edit the same installed skills** → Inspect git/status and file timestamps, keep edits scoped, and do not revert peer changes.

## Migration Plan

1. Add OpenSpec capability and task plan.
2. Update `research-investigation-workflow` references and add audit helpers.
3. Update SourceGuard, TraceGuard, and LogicGuard skill contracts in their source repositories and installed skill folders.
4. Sync project-local skill files and installed Codex skill files.
5. Run quick skill validation, command-surface checks, audit helper smoke tests, OpenSpec validation, and FlowGuard process review.
6. Record postflight notes in the shared KB and relevant run/adoption logs.

## Open Questions

None for this implementation pass. Future package-level schema changes can follow if regression tests show the written contracts and helper scripts are insufficient.
