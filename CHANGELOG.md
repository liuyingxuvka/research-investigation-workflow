# Changelog

## v0.4.3 - 2026-06-07

Guard closure maintenance upgrade.

- Added a research closure helper that aggregates source audit, source-role
  coverage, source portfolio, key-claim ledger, claim-support fit, stale
  evidence, skipped check, and next-action checks into one report.
- Updated the research workflow skill so partial SourceGuard, TraceGuard,
  LogicGuard, or FlowGuard outputs route back to the responsible Guard instead
  of allowing a research task to stop after one pass.
- Added OpenSpec and FlowGuard self-model evidence for the closure-report
  maintenance path.

## v0.4.2 - 2026-06-04

Structural thesis-routing patch.

- Strengthened routing so existing thesis, dissertation, and paper revision tasks with parent-child support, downstream consumer, conclusion recovery, or structural contribution graph work route to `academic-thesis-revision-workflow`.
- Clarified that Research Investigation Workflow can supply evidence discovery, TraceGuard cases, source registries, and Research Reasoning Atlas material to thesis revision without owning the document-revision route.
- Updated public README and skill metadata for the structural routing boundary.

## v0.4.1 - 2026-06-03

Academic thesis revision routing patch.

- Added an explicit handoff to `academic-thesis-revision-workflow` for existing thesis, dissertation, and paper drafts that need DOCX editing, visible revision provenance, original-text rewriting, and chapter/paragraph repair.
- Kept Research Investigation Workflow focused on evidence-led investigations and new research-backed artifacts while allowing its source registries, TraceGuard cases, and reasoning atlases to feed thesis revision work.
- Upgraded the local FlowGuard project record to package version `0.40.8`.

## v0.4.0 - 2026-06-02

Layered research evidence contract upgrade.

- Added source portfolio planning so substantive investigations check primary or closest-available, official/regulatory, execution/outcome, independent, expert/model, counter/limiting, source-lineage, and future-trigger source classes instead of relying on source count alone.
- Added key-claim/key-number ledgers, semantic source-fit checks, and helper scripts for source portfolio, key-number provenance, and claim/source mismatch smoke checks.
- Strengthened TraceGuard and LogicGuard orchestration so important leads, effect chains, sections, paragraphs, slides, and artifact units are modeled at their natural hierarchy before strong final wording.
- Kept final artifact review genre-adaptive, so the workflow judges reports, papers, memos, articles, literature reviews, deck storylines, and decision notes against the user-requested target rather than a fixed report template.

## v0.3.0 - 2026-06-02

Generic Research Reasoning Atlas upgrade.

- Added a domain-neutral Research Reasoning Atlas stage for branch trees, debate matrices, alternative explanations, confounder ledgers, model-lens selection, expert stance maps, causal-chain questions, counterfactual traces, conclusion tournaments, and future falsifiers.
- Routed Atlas branch gaps through SourceGuard, TraceGuard, and LogicGuard so source discovery, trace reconstruction, and final argument audits all preserve competing branches instead of collapsing to one preferred story too early.
- Added generic anti-overfit rules so core skill guidance uses reusable reasoning categories and keeps topic-specific details in selected lenses, examples, or future domain packs.
- Added FlowGuard/OpenSpec model coverage for Atlas ownership, install synchronization, anti-overfit validation, and final quality gates.

## v0.2.2 - 2026-06-02

Research source and citation quality hardening.

- Added source-registry requirements so substantive artifacts keep source ids, roles, freshness clues, locators, access status, and claim use aligned from discovery through final delivery.
- Added final research quality gates for source-role coverage, execution/evidence chains, claim-to-source matrix status, citation consistency, and reader-facing limitation placement.
- Added Markdown citation-marker and source-role coverage helper scripts for lightweight structural audits before final closure.
- Strengthened SourceGuard, TraceGuard, and LogicGuard handoffs around post-draft source gaps, announcement-to-execution chains, semantic citation mismatch, and downgraded conclusion boundaries.

## v0.2.1 - 2026-06-01

Research artifact contract hardening.

- Added requested final artifact genre capture so the workflow can produce reports, papers, memos, briefs, articles, literature reviews, deck storylines, or decision notes without forcing report-only language.
- Added a Research Plan Card and per-round replanning gate for substantive investigations.
- Strengthened SourceGuard discovery-loop guidance with search tactics and source-reading observations.
- Strengthened TraceGuard and LogicGuard handoffs so event facts, explanations, outcomes, evidence roles, gaps, and final prose treatment remain separate.
- Synchronized installed Codex skill guidance and local FlowGuard/OpenSpec validation evidence.

## v0.2.0 - 2026-05-31

SourceGuard discovery orchestration.

- Added SourceGuard as the default source-discovery planner for substantive investigations, before TraceGuard reconstruction and LogicGuard claim modeling.
- Added a SourceGuard discovery loop reference for belief-state setup, ranked search actions, observations, access gaps, backflow, and handoff boundaries.
- Updated workflow, evidence policy, TraceGuard, LogicGuard, output, FlowGuard closure, and History Ledger contracts so missing-source gaps return to SourceGuard or force claim downgrades.
- Updated public README and skill metadata to describe the full SourceGuard, TraceGuard, LogicGuard, FlowGuard, and History Ledger stack.

## v0.1.2 - 2026-05-31

General deep-investigation contract repair.

- Replaced the narrow policy/current-event ladder with a general evidence-role map for claim origin, direct facts, source statements, scope, execution/outcome, context/motive, interpretation, counter/limiting evidence, and future triggers.
- Added mandatory investigation-round guidance for substantive reports: original fact, counter/limiting, impact/execution, stakeholder, and future-trigger rounds.
- Added reader-facing report cleanup and downgrade rules so incomplete rounds cannot be labeled as complete reports and internal Guard-family terms stay out of the main report.
- Updated OpenSpec evidence for the generalized upgrade while preserving FlowGuard as a process/freshness/privacy tool only.

## v0.1.1 - 2026-05-31

Policy-rumor investigation audit hardening.

- Added a policy/current-event evidence ladder for trigger claims, official actions, jurisdiction/scope, implementation signals, market data, fiscal context, expert commentary, and forecasts.
- Added source-role freshness and claim-use checks to the evidence, output, FlowGuard closure, and History Ledger contracts.
- Strengthened report readability requirements with reader routes, section handoffs, paragraph jobs, and missing implementation-signal disclosure.
- Added OpenSpec evidence for the real-run repair pass while keeping local investigation outputs ignored.

## v0.1.0 - 2026-05-31

Initial public source release.

- Added the `research-investigation-workflow` Codex skill as a thin orchestration layer over TraceGuard, LogicGuard, and FlowGuard.
- Added reference contracts for workflow staging, evidence-source policy, TraceGuard lead loops, LogicGuard report synthesis, FlowGuard closure, History Ledger use, and final output shape.
- Added an OpenSpec-backed deep-investigation contract: investigation depth is measured by logic leads and evidence chains, not source counts or shallow/medium/deep modes.
- Added local-output privacy boundaries so reports, TraceGuard cases, LogicGuard source libraries, and History Ledger records stay local and ignored unless explicitly sanitized for publication.
- Added FlowGuard adoption records and validation models for implementation closure.
