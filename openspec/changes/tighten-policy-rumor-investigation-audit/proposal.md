## Why

The first real policy-rumor investigation showed that the upgraded workflow can produce citation-backed reports, but it still needs more explicit guardrails for current-event policy rumors where official action, local pilot changes, market interpretation, fiscal pressure, and expert commentary are easy to blur. This change turns that run lesson into reusable skill behavior without creating a new reasoning engine.

## What Changes

- Add a policy-rumor/event ladder to `research-investigation-workflow`: separate trigger claim, official action, jurisdiction/scope, implementation evidence, market data, fiscal or motive context, expert commentary, and future hypothesis.
- Require negative and partial findings to show which implementation signals were checked before writing that something is not supported.
- Strengthen report readability requirements: long reports must include a reader route, section handoffs, and paragraph jobs before final prose.
- Strengthen source-link hygiene: source ids must carry role, date/freshness, claim use, and citation coverage; bibliography-only support remains invalid for important claims.
- Strengthen TraceGuard guidance so motive/fiscal/context evidence cannot be mistaken for implementation or outcome evidence.
- Strengthen LogicGuard guidance so source-backed report writing audits the difference between fact, official claim, analysis, and forecast after the final material edit.
- Keep FlowGuard as the process/freshness closure layer used by this skill; do not modify standalone FlowGuard behavior.
- Sync every changed skill source to its installed Codex skill surface and commit only software/skill-source changes, not local investigation reports or private ledgers.

## Capabilities

### New Capabilities

- `policy-rumor-investigation-audit`: Adds reusable investigation requirements for policy rumors and current-event claims where an apparent "new event" may be a mix of official actions, local pilots, market data, fiscal context, expert commentary, and unsupported extrapolation.

### Modified Capabilities

- None. There are no active baseline OpenSpec specs in this repository.

## Impact

- Affects the project-local and installed `research-investigation-workflow` skill.
- Affects TraceGuard skill guidance for event/implementation/fiscal-motive separation and safe handoff wording.
- Affects LogicGuard skill guidance for final report/source-role/citation audit.
- Affects OpenSpec and FlowGuard validation evidence in the research workflow repository.
- Does not affect UI, public APIs, runtime packages, or standalone FlowGuard skill behavior.
