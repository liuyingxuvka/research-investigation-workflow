## Context

`research-investigation-workflow` is a thin orchestration skill over existing Guard-family tools. The existing workflow already has SourceGuard discovery planning, TraceGuard evidence-to-storyline reconstruction, LogicGuard claim/source synthesis, FlowGuard closure, and History Ledger memory.

The upgrade is not a product/UI change. The requested improvement is a behavior-contract upgrade: learn from ChatGPT Deep Research's stronger research planning and iterative direction changes while preserving Guard-family strengths and keeping final output shaped by the user's requested artifact type.

## Goals / Non-Goals

**Goals:**

- Make substantive investigations start with an explicit research plan card.
- Make each meaningful search/source-reading batch end with a replanning decision.
- Expand SourceGuard guidance with a search tactic catalog and source-reading observation contract.
- Make TraceGuard preserve event fact, explanation, and outcome boundaries.
- Make LogicGuard preserve target artifact genre while enforcing claim-to-source and claim-to-prose coverage.
- Replace report-only language in the research output contract with final artifact / target artifact language.
- Sync installed Codex skills after source repo edits.

**Non-Goals:**

- Do not build a standalone app, UI, progress dashboard, one-command runner, crawler, or new reasoning engine.
- Do not make SourceGuard perform external search itself.
- Do not make TraceGuard write final truth claims.
- Do not force LogicGuard final outputs into a fixed list style such as fact / official claim / inference / gap headings.
- Do not change FlowGuard's generic skill; only use it for process closure and validation evidence.

## Decisions

1. **Use target artifact instead of report as the top-level delivery concept.**  
   Rationale: Research work may produce a report, paper, memo, brief, article, deck storyline, or another artifact. The workflow must enforce support coverage without imposing one visible style.

2. **Treat source-role categories as internal coverage obligations.**  
   Rationale: Event facts, official claims, inference, limitations, and gaps must be tracked, but they need not become visible headings. The requested genre controls prose organization.

3. **Add replanning as a workflow gate, not a UI.**  
   Rationale: The borrowed strength from deep research is iterative research behavior, not product chrome. A simple required decision after each meaningful batch is sufficient.

4. **Keep SourceGuard, TraceGuard, and LogicGuard boundaries intact.**  
   Rationale: SourceGuard ranks search value, TraceGuard reconstructs evidence-backed storylines, and LogicGuard checks final claim support. Blurring these boundaries would weaken auditability.

5. **Start with skill/reference contract changes before Python schema changes.**  
   Rationale: Most current gaps are orchestration and agent-behavior gaps. CLI/schema work should follow only if real-task regression shows the written contract is not stable enough.

## Risks / Trade-offs

- **Risk: More gates slow small tasks** → Apply the full contract only to substantive investigation work and keep cards lightweight.
- **Risk: Final artifacts become checklist-like** → Require genre-preserving synthesis and move matrices/audits to appendix when they would break the requested artifact.
- **Risk: Installed skills drift from source repos** → Sync source and installed skill folders, then validate both paths.
- **Risk: Concurrent AI changes are overwritten** → Check git status before/after and limit edits to targeted skill/reference files.
- **Risk: SourceGuard no OpenSpec repo** → Track cross-skill requirements in the orchestrator OpenSpec change and validate SourceGuard with AGENTS-required commands.

## Migration Plan

1. Update OpenSpec proposal/design/spec/tasks in `ResearchInvestigationWorkflow_20260531`.
2. Patch source repo skill/reference files for research workflow, SourceGuard, TraceGuard, and LogicGuard.
3. Sync the corresponding installed Codex skill folders under `C:\Users\liu_y\.codex\skills`.
4. Run skill validation, focused command-surface checks, OpenSpec validation, FlowGuard checks, and package examples/tests.
5. Record FlowGuard adoption evidence and final git status without reverting other agents' work.

## Open Questions

None for implementation. If later real-task regression shows the contract is not stable enough, a follow-up change can add schema fields such as SourceGuard tactic type, SourceGuard source-reading support fields, TraceGuard three-layer lead status, or LogicGuard final prose treatment.
