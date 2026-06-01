## Why

The research workflow already coordinates SourceGuard, TraceGuard, LogicGuard, FlowGuard, and run history, but it still needs a tighter contract for deep-research style planning, round-by-round replanning, and genre-preserving final artifacts. The current wording can over-focus on "reports", while the user may request a paper, memo, brief, article, deck storyline, or another research-backed artifact.

## What Changes

- Add a research plan card before substantive investigation work begins.
- Add a per-round replanning gate after meaningful search or source-reading batches.
- Expand SourceGuard-facing guidance with reusable search tactics and source-reading observation fields.
- Strengthen TraceGuard-facing guidance so event facts, explanations, and outcomes are not collapsed into one claim.
- Strengthen LogicGuard-facing guidance so final artifact synthesis preserves the requested genre while still enforcing claim-to-source and claim-to-prose coverage.
- Update output and closure contracts to say "target artifact" or "final artifact" instead of assuming a report-only deliverable.
- Sync project-local skills and installed Codex skills after implementation.

## Capabilities

### New Capabilities

- `research-artifact-contract`: Defines planning, replanning, evidence-role coverage, genre-preserving final artifact synthesis, and final artifact closure for research-investigation-workflow.

### Modified Capabilities

- None. This repository has no active top-level OpenSpec specs; the new capability captures this upgrade's requirement contract.

## Impact

- Affects `skills/research-investigation-workflow/SKILL.md` and reference contracts.
- Affects installed `research-investigation-workflow` skill sync.
- Coordinates source-skill wording updates in local SourceGuard, TraceGuard, and LogicGuard source repositories plus installed Codex skill folders.
- Does not add a UI, standalone app, one-command runner, crawler, truth engine, or fixed report style.
