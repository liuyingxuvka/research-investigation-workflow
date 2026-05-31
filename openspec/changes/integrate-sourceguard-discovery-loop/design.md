## Context

The workflow already orchestrates TraceGuard, LogicGuard, FlowGuard, and the Research Investigation History Ledger. Its current weak point is the source-discovery phase: first-round search and gap-driven search are described as rule lists, but there is no explicit planner that ranks public/local/internal search actions, records permission gaps, or keeps multimodal anchor needs separate from evidence claims.

SourceGuard is now installed locally as a Codex skill and Python package. It provides the missing discovery layer without creating a new truth engine.

## Goals / Non-Goals

**Goals:**

- Make SourceGuard the default discovery planner for substantive `research-investigation-workflow` runs.
- Insert SourceGuard before first-round search and inside the TraceGuard gap-driven loop.
- Preserve all source-access classes: public, local, internal, permission-gated, and hypothesis/inference.
- Convert TraceGuard gaps into SourceGuard search actions and observations.
- Keep SourceGuard utility scores out of final claim confidence.
- Sync project-local and installed skill copies after edits.

**Non-Goals:**

- Do not make SourceGuard perform external search by itself.
- Do not replace TraceGuard event/storyline modeling.
- Do not replace LogicGuard final argument audit.
- Do not modify FlowGuard itself.
- Do not publish local investigation outputs, private case libraries, or internal evidence.

## Decisions

1. **Use SourceGuard as a discovery layer, not a top-level orchestrator.**
   - Rationale: `research-investigation-workflow` remains the overall investigation skill; SourceGuard only owns "what to search next".
   - Alternative rejected: Replace the whole gap-driven loop with SourceGuard. That would blur TraceGuard and LogicGuard responsibilities.

2. **Add a dedicated reference file.**
   - Rationale: SKILL.md must stay concise. The detailed loop belongs in `references/sourceguard-discovery-loop.md`.
   - Alternative rejected: Inline all SourceGuard detail into SKILL.md, which would bloat the trigger-loaded context.

3. **Route gaps backward from TraceGuard to SourceGuard.**
   - Rationale: TraceGuard is best at discovering missing event, contradiction, timeline, and evidence-chain gaps; SourceGuard is best at turning those gaps into next search actions.
   - Alternative rejected: Let TraceGuard own search planning directly, which duplicates SourceGuard's purpose.

4. **Promote only selected candidates into LogicGuard.**
   - Rationale: LogicGuard should model durable support, not raw search results or weak clue piles.
   - Alternative rejected: Bulk-copy all SourceGuard material into LogicGuard, which would pollute formal source libraries.

## Risks / Trade-offs

- **Risk: workflow becomes too heavy for small questions** → Mitigation: SourceGuard is a default for this heavy investigation skill, not every casual answer.
- **Risk: utility score is mistaken for truth** → Mitigation: repeat the boundary in SKILL.md, SourceGuard reference, output contract, and LogicGuard promotion guidance.
- **Risk: local/internal search leaks private material** → Mitigation: keep source-policy classification before execution and record internal material by pointer/role rather than copying private content into public outputs.
- **Risk: installed skill drifts from repository skill** → Mitigation: copy project-local skill to installed path and verify parity before release.
- **Risk: publication includes run artifacts** → Mitigation: check `.gitignore`, `git status`, and release diff before commit/push.

## Migration Plan

1. Update OpenSpec artifacts and validate the change.
2. Patch project-local `skills/research-investigation-workflow` references.
3. Sync project-local skill to `$CODEX_HOME/skills/research-investigation-workflow`.
4. Update README, VERSION, and CHANGELOG for release `v0.2.0`.
5. Validate with targeted text checks, skill validation, FlowGuard project audit, OpenSpec validation, and installed/project parity.
6. Commit, tag, push, and create GitHub release.
