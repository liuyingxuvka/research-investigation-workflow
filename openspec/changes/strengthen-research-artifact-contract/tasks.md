## 1. Research Workflow Contract

- [x] 1.1 Update `research-investigation-workflow` SKILL.md to use target artifact language instead of report-only delivery language.
- [x] 1.2 Add Research Plan Card guidance to `references/workflow.md`.
- [x] 1.3 Add per-round replanning gate guidance to `references/workflow.md`.
- [x] 1.4 Update `references/output-contract.md` to define final artifact delivery by requested genre.
- [x] 1.5 Update `references/flowguard-closure.md` to audit final artifact language rather than report-only language.

## 2. SourceGuard and TraceGuard Contract

- [x] 2.1 Update SourceGuard source skill guidance with search tactic catalog and source-reading observation contract.
- [x] 2.2 Update SourceGuard installed skill guidance to match the source skill.
- [x] 2.3 Update TraceGuard source skill guidance with event / explanation / outcome separation and LogicGuard handoff completeness.
- [x] 2.4 Update TraceGuard installed skill guidance to match the source skill.

## 3. LogicGuard Contract

- [x] 3.1 Update LogicGuard main skill guidance with genre-preserving synthesis and claim-to-prose coverage.
- [x] 3.2 Update LogicGuard artifact synthesis skill guidance with genre-preserving final artifact rules.
- [x] 3.3 Update LogicGuard structured artifact skill guidance with target artifact mapping and audit rules.
- [x] 3.4 Sync installed LogicGuard skill folders to match source skill folders.

## 4. Sync and Validation

- [x] 4.1 Sync `research-investigation-workflow` installed skill from source.
- [x] 4.2 Validate all changed installed skill folders with `quick_validate.py`.
- [x] 4.3 Validate OpenSpec change artifacts.
- [x] 4.4 Run FlowGuard project checks for affected repositories that have FlowGuard project records.
- [x] 4.5 Run focused command-surface/package checks for SourceGuard, TraceGuard, and LogicGuard.
- [x] 4.6 Record FlowGuard adoption evidence for the staged update.
- [x] 4.7 Check git status in all affected repositories without reverting peer-agent changes.

Validation notes:

- Research workflow FlowGuard valid path passed; built-in broken/stale fixture paths still block as expected.
- SourceGuard FlowGuard project record was adopted, then project audit passed.
- LogicGuard satellite routing FlowGuard model was refreshed with current TestMesh split evidence and now passes.
- Source, Trace, and Logic command surfaces passed focused checks; installed skill files match source files by hash.
