## Why

The research workflow already has several helper checks, but they are independent and can be skipped or interpreted inconsistently. A single closure helper makes citation, source-role, portfolio, key-claim, semantic-fit, stale-evidence, and downstream Guard gaps visible before final delivery.

## What Changes

- Add aggregate research closure helper.
- Update the research skill to require the closure helper before final investigation claims.
- Route failed helper checks to SourceGuard, TraceGuard, LogicGuard, or FlowGuard next actions.

## Capabilities

### New Capabilities
- `guard-closure-contract`: Research investigation closure ledger and aggregate closure report.

### Modified Capabilities
- None.

## Impact

Affected surfaces: `research-investigation-workflow` skill, helper scripts, installed skill sync.
