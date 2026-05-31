## Why

Long-running research and investigation tasks need a repeatable Codex workflow that keeps messy evidence, formal source support, process closure, and reusable run history separate. The project already defines the Guard-family basis, so the first implementation should package that plan as an installable skill rather than inventing another reasoning engine.

## What Changes

- Add a new Codex skill named `research-investigation-workflow`.
- Define a concise `SKILL.md` that triggers on research, investigation, evidence collection, report synthesis, and Guard-family orchestration requests.
- Add reference files for the end-to-end workflow, evidence-source policy, TraceGuard loop, LogicGuard synthesis, FlowGuard closure, History Ledger, and final output contract.
- Add `agents/openai.yaml` metadata for the skill UI.
- Keep TraceGuard Case Library, LogicGuard Source Library, FlowGuard process records, and Research Investigation History Ledger as separate memory layers.
- Validate the installed skill and perform a manual smoke review against the acceptance criteria.

## Capabilities

### New Capabilities

- `research-investigation-workflow`: Defines the orchestration behavior, boundaries, history-ledger rules, and output contract for multi-round investigations built on TraceGuard, LogicGuard, and FlowGuard.

### Modified Capabilities

- None.

## Impact

- Creates an installed skill under `C:\Users\liu_y\.codex\skills\research-investigation-workflow`.
- Adds a synchronized project copy for local repository review.
- Adds OpenSpec artifacts for this implementation in `openspec/changes/add-research-investigation-workflow-skill`.
- Does not add a UI, standalone service, database server, new reasoning engine, or merged evidence/source store.
