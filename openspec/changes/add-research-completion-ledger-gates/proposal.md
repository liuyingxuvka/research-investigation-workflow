## Why

The research workflow already has strong closure helpers, but the top-level
skill should make the common completion ledger explicit so child Guard evidence
cannot disappear into prose-only summaries.

## What Changes

- Add a top-level completion ledger rule for research runs.
- Require child Guard rows for SourceGuard, TraceGuard, LogicGuard, and
  FlowGuard when they are used or intentionally skipped.
- Clarify that final research closure follows the weakest important row.

## Capabilities

### New Capabilities
- `research-completion-ledger-gates`: Top-level completion ledger rows for
  research investigations.

### Modified Capabilities
- `guard-closure-contract`: Clarify how child Guard rows feed the aggregate
  closure report.

## Impact

- Updates `skills/research-investigation-workflow/SKILL.md`.
- Keeps existing helper scripts unchanged.
