## Why

The current research workflow is strong at source coverage, execution-chain separation, and final citation audits, but it still risks producing a mostly linear report when the user wants research quality far beyond ordinary deep-research output. The next upgrade should make the system expand and judge a broad generic reasoning space: pro, con, alternatives, causal paths, counterfactuals, expert stances, transferable model lenses, and conclusion competition.

This must be a general research upgrade, not a domain-specific upgrade for AI data centers, energy, finance, policy, or any single report topic. Domain examples may be used as tests only; the skill rules must stay abstract and reusable across future investigations.

## What Changes

- Add a general Research Reasoning Atlas contract to `research-investigation-workflow`.
- Require a generic branch tree before substantial research writing: support branches, opposing branches, alternative explanations, confounders, stakeholder branches, temporal/geographic/scope branches, falsifiers, and future triggers.
- Add model-lens selection as a generic step: choose transferable analytical lenses from the topic type without hard-coding any domain-specific checklist into the core skill.
- Add expert-stance mapping as a generic research obligation when expert interpretation materially affects the report.
- Upgrade SourceGuard to plan search by branch, disconfirming value, source diversity, source lineage, expert/model support, and generic source-role coverage.
- Upgrade TraceGuard to preserve competing storylines, causal-chain states, counterfactual traces, confounder ledgers, and red-team storylines.
- Upgrade LogicGuard to judge competing conclusions, steelman opposing views, model lenses as warrants, expert claims as typed support, and stress-test conclusion robustness.
- Keep domain-specific lenses as optional future reference packs or examples, not as main-skill requirements.
- Sync local source skill files, installed Codex skill copies, versions, changelogs, and validation records after implementation.

## Capabilities

### New Capabilities
- `research-reasoning-atlas`: General reasoning-map capability for deep research workflows, covering branch explosion, pro/con and alternative explanation matrices, model-lens selection, expert-stance mapping, branch-aware source discovery, competing traces, counterfactual reasoning, and conclusion tournament audits.

### Modified Capabilities

None. No archived specs currently exist in this repository; this change introduces a new generic capability.

## Impact

- Affected source skills:
  - `skills/research-investigation-workflow`
  - SourceGuard repository `skills/sourceguard`
  - TraceGuard repository `SKILL.md`
  - TraceGuard repository `skills/traceguard-library`
  - LogicGuard repository `skills/logicguard`
  - selected LogicGuard satellite skills whose direct routes must not bypass the new audit boundary.
- Affected installed Codex skill copies under the user's local Codex skills directory.
- Affected version/changelog files in the local source repositories.
- No new core reasoning engine is introduced; the upgrade extends the orchestration and handoff contracts of existing Guard-family workflows.
