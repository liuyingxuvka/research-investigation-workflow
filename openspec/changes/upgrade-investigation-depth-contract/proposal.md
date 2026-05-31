## Why

The first real run of `research-investigation-workflow` produced a usable report, but it did not dig deeply enough through the full logic leads, did not attach citations to each important claim in the body, and left section-to-section reasoning too loose. The skill needs a stronger deep-investigation contract while preserving its thin orchestration role over TraceGuard, LogicGuard, and FlowGuard.

## What Changes

- Make deep investigation the default behavior for this skill; do not add shallow/medium/deep modes or use source counts as the primary depth measure.
- Require a minimum set of investigation rounds for substantive reports: official/original fact, counter/limiting, impact/execution, stakeholder, and future-trigger. Incomplete rounds force downgraded closure rather than "complete report" wording.
- Replace the earlier policy-rumor ladder with a general evidence-role map covering claim origin, direct facts, source statements, scope, execution/outcome, context/motive, interpretation, counter/limiting evidence, and future triggers.
- Require a logic-lead map for every substantive investigation: each major causal, actor, motive, outcome, contradiction, and future-impact line must have a status, support, counter/support-limiting evidence, open gaps, and report eligibility.
- Strengthen TraceGuard usage to produce event chains, explanation leads, evidence-chain states, contradiction/gap ledgers, and gap-driven follow-up searches before final writing.
- Strengthen LogicGuard usage to require claim-to-source matrices, paragraph/section blueprints, inline citation markers, source-role labels, and final prose audit for every important claim.
- Keep FlowGuard as a process/freshness tool and do not change the FlowGuard skill itself. Add stricter FlowGuard closure rules inside `research-investigation-workflow` for logic-lead coverage, citation completeness, final-audit freshness, and local-output privacy.
- Clean the reader-facing main report so Guard-family tool names remain in appendices or local run records unless the user asks for methodology detail.
- Keep investigation outputs local-only by default: reports, TraceGuard cases, LogicGuard source libraries, and History Ledger records must not be committed to the software repository unless the user explicitly requests a sanitized published sample.
- Sync every upgraded skill surface between installed skill folders and local repository mirrors, and commit only software/skill source changes to the relevant local Git repositories.

## Capabilities

### New Capabilities

- `deep-investigation-contract`: Defines the default deep-investigation behavior, logic-lead coverage, evidence-chain depth, citation requirements, report structure, and closure/privacy rules for investigation runs.

### Modified Capabilities

- None. There are no active baseline OpenSpec specs in this repository to delta.

## Impact

- Affects the installed and project-local `research-investigation-workflow` skill.
- Affects installed/local TraceGuard skill guidance for logic-lead and evidence-chain handoff.
- Affects installed/local LogicGuard skill guidance and relevant satellite guidance for citation-grounded report writing, section/paragraph blueprints, and claim-to-source audit.
- Does not modify FlowGuard skill behavior; only the `research-investigation-workflow` reference for FlowGuard closure usage is updated.
- Affects validation expectations: quick skill validation, OpenSpec strict validation, FlowGuard project audit, and focused content checks for citation/depth/privacy instructions.
