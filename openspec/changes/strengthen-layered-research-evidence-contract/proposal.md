## Why

The first real report comparison showed that the research workflow is careful about evidence boundaries but does not yet reliably force broad source portfolios, key-number provenance, semantic source-fit checks, or deeply layered LogicGuard/TraceGuard modeling before final artifacts. This change strengthens the contract so a substantive investigation can produce both auditable evidence discipline and artifact-native final outputs for the user's requested genre.

## What Changes

- Require a source portfolio plan that checks high-value source classes instead of relying on whatever sources were found first.
- Require a key-claim and key-number ledger that records source, date, role, support boundary, and unsupported overclaim wording.
- Require impact, causal, price, policy, or market-effect claims to pass through an explicit transmission/effect chain before final wording.
- Require hierarchical LogicGuard modeling for substantive artifacts: document -> section -> paragraph or artifact unit -> local claim/evidence/warrant/limitation.
- Require hierarchical TraceGuard modeling for substantive investigations: lead -> event/explanation/outcome layers -> execution chain -> competing storyline/counterfactual/confounder status.
- Require final artifact review to adapt to the user-requested genre, not to a fixed "report-like" style.
- Add lightweight ledger templates and deterministic check helpers for source portfolio coverage, key-claim ledger completeness, and claim/source semantic fit.
- Sync the upgraded source skill files to installed Codex skill folders without modifying FlowGuard's own skill behavior.

## Capabilities

### New Capabilities

- `layered-research-evidence-contract`: Contract for source portfolio coverage, key-claim ledgers, transmission/effect chains, hierarchical Guard modeling, genre-adaptive synthesis, and deterministic helper checks in research investigations.

### Modified Capabilities

- None.

## Impact

- Affects `skills/research-investigation-workflow` guidance, references, templates, and helper scripts.
- Affects installed and source guidance for `sourceguard`, `traceguard`, and `logicguard`.
- Adds research workflow templates and helper scripts; does not add a crawler, new reasoning engine, UI, or FlowGuard behavior change.
- Requires validation through OpenSpec, skill quick validation, helper smoke tests, command-surface checks, and FlowGuard DevelopmentProcessFlow evidence.
