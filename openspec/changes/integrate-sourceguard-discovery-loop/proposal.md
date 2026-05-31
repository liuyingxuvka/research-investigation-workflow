## Why

`research-investigation-workflow` already treats investigation as heavy, evidence-led work, but its search phases are still described as broad manual search rounds. SourceGuard now provides the missing source-discovery planner: it can turn evidence gaps into ranked search actions, preserve candidate sources and anchors, and keep search value separate from factual confidence.

## What Changes

- Add SourceGuard as the default source-discovery layer for substantive investigations.
- Require initial SourceGuard belief-state planning before first-round search.
- Route TraceGuard gaps back into SourceGuard for evidence-seeking, counter/limiting search, multimodal anchor search, local/internal search, and permission-gap handling.
- Require observations from public, local, internal, and permission-gated searches to be recorded as SourceGuard candidate sources and evidence anchors before TraceGuard or LogicGuard promotion.
- Keep LogicGuard promotion selective: LogicGuard receives stable SourceGuard/TraceGuard-selected candidates, not raw search results.
- Preserve the existing boundaries: SourceGuard does not prove facts, TraceGuard does not audit final arguments, LogicGuard does not store messy case evidence, and FlowGuard owns process freshness and closure.

## Capabilities

### New Capabilities

- `sourceguard-discovery-orchestration`: SourceGuard-first source discovery planning, observation update, gap backflow, multimodal anchor handling, and handoff into TraceGuard/LogicGuard inside the investigation workflow.

### Modified Capabilities

- `research-investigation-workflow`: The main investigation workflow now requires SourceGuard as the default discovery planner for heavy evidence work.
- `deep-investigation-contract`: Substantive investigation rounds must use SourceGuard planning for search direction selection and downgrade decisions when key source gaps remain.

## Impact

- Affects `skills/research-investigation-workflow/SKILL.md`.
- Adds a new reference file for SourceGuard discovery loops.
- Updates workflow, evidence policy, TraceGuard loop, LogicGuard synthesis, output contract, README, changelog, version, and installed skill copy.
- Requires local skill validation, install-sync comparison, FlowGuard process review, GitHub push, and release publication.
