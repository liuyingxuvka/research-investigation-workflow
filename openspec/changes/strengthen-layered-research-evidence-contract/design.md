## Context

`research-investigation-workflow` already coordinates SourceGuard for discovery, TraceGuard for evidence/storyline reconstruction, LogicGuard for argument and citation audit, and FlowGuard for process freshness. The comparison between a local Markdown investigation and a separate Deep Research PDF showed that the current workflow is strong at source-role caution but weaker at consistently forcing broad high-value source discovery, numeric provenance, semantic source-fit review, layered Guard modeling, and artifact-native final synthesis.

The user also clarified that LogicGuard must not apply a fixed "does this look like a report" standard. It must adapt to the requested artifact genre, such as report, paper, memo, article, literature review, deck storyline, or decision note.

## Goals / Non-Goals

**Goals:**

- Add a source portfolio contract so high-value source classes are planned and checked before final drafting.
- Add key-claim and key-number ledgers so material figures and conclusions carry provenance, support boundary, and unsafe overclaim wording.
- Add transmission/effect-chain handling for price, market, policy, causal, adoption, execution, or impact claims.
- Make hierarchical LogicGuard and TraceGuard modeling a required deep-use pattern for substantive artifacts.
- Keep final synthesis genre-adaptive and user-goal-specific.
- Add deterministic helper scripts for structural checks that can run before final closure.
- Sync changed source skill files and installed skill folders without modifying FlowGuard itself.

**Non-Goals:**

- Do not create a new reasoning engine.
- Do not add web crawling, OCR, UI, dashboards, or package schema migrations.
- Do not hard-code domain-specific source lists into the universal skill.
- Do not make SourceGuard decide factual truth, TraceGuard write final conclusions, or LogicGuard store messy case evidence.
- Do not require diagnostic tables in reader-facing final artifacts when the requested genre does not benefit from them.

## Decisions

1. **Keep capability in the research orchestration layer, with source skill guidance mirrored in each owning skill.**  
   Rationale: The cross-skill behavior belongs to the research workflow, but SourceGuard, TraceGuard, and LogicGuard need their own guidance so direct use of those skills remains consistent. Alternative considered: only change the research workflow. Rejected because direct SourceGuard/TraceGuard/LogicGuard calls would miss the new contract.

2. **Use lightweight ledgers and deterministic scripts before package-level schema changes.**  
   Rationale: The requested upgrade is mostly workflow contract and artifact quality. YAML/JSON/Markdown ledgers plus helper scripts can validate missing coverage and semantic-fit risks without changing runtime packages. Alternative considered: add first-class CLI model fields in all Guard packages. Deferred because it is heavier and not necessary for this pass.

3. **Model hierarchy by artifact unit rather than by one global root claim only.**  
   Rationale: Substantive writing fails at section and paragraph level as often as at conclusion level. LogicGuard must inspect document/section/paragraph or slide/unit relationships, while TraceGuard must inspect lead/event/explanation/outcome/execution layers. Alternative considered: only strengthen final conclusion tournament. Rejected because it would still allow unsupported paragraphs.

4. **Make final artifact review genre-adaptive.**  
   Rationale: A report, paper, deck storyline, memo, and article have different delivery standards. The final audit must check conformance to the user-requested artifact profile, not impose a universal report style.

5. **Use FlowGuard only for lifecycle freshness.**  
   Rationale: The user explicitly excluded FlowGuard as a report-writing rule owner. FlowGuard will track changed artifacts, validation evidence, stale checks, sync status, and closure boundaries only.

## Risks / Trade-offs

- **More intermediate ledgers can slow small tasks** -> Apply the full contract only to substantive source-backed investigations; quick answers remain downgraded as initial leads or working hypotheses.
- **Final artifacts may become too diagnostic** -> Keep ledgers and matrices internal, appendix-only, or local unless the requested artifact benefits from visible tables.
- **Semantic-fit checks cannot prove truth automatically** -> Treat helper results as structural warnings; LogicGuard still owns exact wording review.
- **Cross-repo sync can drift** -> Edit source repositories first, then copy matching files to installed skill folders and validate parity.
- **Peer agent edits may race** -> Check git status before and after meaningful write batches; do not revert unknown changes.

## Migration Plan

1. Add this OpenSpec change and tasks.
2. Update `research-investigation-workflow` SKILL and references with source portfolio, key-claim ledger, effect-chain, layered modeling, and genre-adaptive synthesis contracts.
3. Add templates and helper scripts under the research workflow skill.
4. Update SourceGuard skill guidance for source portfolios, numeric provenance search, independence checks, and post-draft gap backflow.
5. Update TraceGuard skill guidance for layered evidence models, effect chains, announcement-to-outcome funnels, scope-transfer checks, confounder ledgers, and safe/unsafe wording.
6. Update LogicGuard skill guidance for hierarchical artifact modeling, semantic source-fit audit, key-claim ledger use, central conclusion tournaments, and genre-adaptive final artifact review.
7. Sync source and installed skill folders.
8. Run OpenSpec validation, quick skill validation, helper smoke tests, command-surface checks, and FlowGuard DevelopmentProcessFlow checks.

## Open Questions

None for this implementation pass.
