## ADDED Requirements

### Requirement: Generic Research Reasoning Atlas
The system SHALL support a general Research Reasoning Atlas for substantive research artifacts. The Atlas MUST map important reasoning branches, support and opposition, alternatives, confounders, analytical lenses, expert stances, causal chains, counterfactual traces, and conclusion comparisons without encoding domain-specific checklists in the core skill rules.

#### Scenario: Atlas uses generic primitives
- **WHEN** a user requests a substantive research report, memo, paper, brief, article, deck storyline, or decision note
- **THEN** the workflow creates or simulates a generic Atlas using transferable primitives rather than topic-specific fixed prompts

#### Scenario: Domain details remain outside the core
- **WHEN** a domain example such as energy, finance, medicine, company strategy, policy, or technology is used to test the workflow
- **THEN** the core skill text remains framed in generic categories such as external drivers, alternative explanations, scope boundaries, implementation signals, stakeholder impacts, and falsifiers

### Requirement: Branch Tree Expansion
The system SHALL build a branch tree before broad final writing for substantive investigations. The branch tree MUST include support branches, opposing branches, alternative explanations, confounders, stakeholder branches when relevant, temporal/scope branches when relevant, falsifying evidence, and future trigger conditions.

#### Scenario: Important conclusion has branches
- **WHEN** the workflow identifies a core claim or conclusion candidate
- **THEN** it records supporting, opposing, alternative, and falsifying branches or explicitly downgrades the claim if branch expansion is not feasible

#### Scenario: Branches are not counted blindly
- **WHEN** many branches are generated
- **THEN** each branch carries a relevance or claim-impact label so the final artifact is not rewarded for low-value branch volume

### Requirement: Debate And Alternative Explanation Matrix
The system SHALL maintain a debate matrix for important conclusions. The matrix MUST record the strongest support, strongest opposition, alternative explanations, current adjudication, missing evidence, and final writing treatment.

#### Scenario: Strong claim requires opposition
- **WHEN** a final artifact states a strong or central conclusion
- **THEN** the matrix includes the strongest opposing or limiting case and the reason it does or does not defeat the conclusion

#### Scenario: Alternative explanation remains viable
- **WHEN** an alternative explanation has unresolved material support
- **THEN** the final claim strength is downgraded or the alternative is presented as an unresolved competing explanation

### Requirement: Model Lens Selection
The system SHALL select transferable analytical model lenses when they can materially improve reasoning. A lens MUST generate at least one branch, warrant, evidence need, limitation, or falsifier; it MUST NOT appear as a decorative framework name only.

#### Scenario: Lens generates research obligations
- **WHEN** a model lens is selected
- **THEN** the workflow records what the lens adds to the branch tree, source plan, trace model, or argument audit

#### Scenario: Domain lens is optional and scoped
- **WHEN** a domain-specific model lens is useful
- **THEN** it is treated as an optional selected lens or future lens pack, not as a universal core requirement

### Requirement: Expert Stance Mapping
The system SHALL map expert or institution views when expert interpretation materially affects the conclusion. Expert stances MUST be typed as factual evidence, interpretation, forecast, stakeholder statement, method lens, disputed claim, or background context.

#### Scenario: Experts disagree
- **WHEN** expert or institutional views conflict
- **THEN** the workflow groups the stance families, identifies what each family supports or contests, and prevents the final artifact from treating expert interpretation as direct fact

#### Scenario: Expert source has limited role
- **WHEN** an expert source provides interpretation rather than direct evidence
- **THEN** the final claim or LogicGuard audit preserves that role boundary

### Requirement: Branch-Aware Source Discovery
SourceGuard SHALL plan evidence discovery by branch and disconfirming value. Search actions MUST identify the branch, source role, expected disconfirmation or confirmation value, source diversity need, source-lineage concern, and handoff readiness when applicable.

#### Scenario: Search targets a branch gap
- **WHEN** a branch lacks support, opposition, alternative-explanation evidence, expert/model support, or falsifier evidence
- **THEN** SourceGuard proposes targeted actions tied to that branch rather than a generic keyword-only search plan

#### Scenario: Source lineage prevents false diversity
- **WHEN** multiple candidate sources appear to repeat the same underlying origin
- **THEN** SourceGuard records the lineage/dependency risk and does not treat them as fully independent support

### Requirement: Competing Trace And Counterfactual Reconstruction
TraceGuard SHALL preserve competing storylines, causal-chain state, counterfactual traces, confounder ledgers, and red-team storylines when important claims depend on chronology, causality, execution, impact, or competing explanations.

#### Scenario: Multiple storylines remain possible
- **WHEN** evidence supports more than one plausible storyline
- **THEN** TraceGuard records each storyline's support, gaps, contradictions, safe wording, unsafe wording, and next evidence need

#### Scenario: Counterfactual changes claim strength
- **WHEN** a counterfactual path suggests the outcome may occur without the proposed main cause
- **THEN** TraceGuard records the causal uncertainty and routes it to LogicGuard for conclusion adjudication or to SourceGuard for more evidence

### Requirement: Conclusion Tournament Audit
LogicGuard SHALL run or simulate a conclusion tournament for important conclusions. The tournament MUST compare the preferred conclusion against steelman opposing views and material alternatives using evidence support, warrants, assumptions, rebuttals, scope, model lenses, expert-role boundaries, and robustness tests.

#### Scenario: Preferred conclusion wins narrowly
- **WHEN** the preferred conclusion is better supported but material alternatives remain live
- **THEN** LogicGuard recommends qualified wording rather than a conclusive claim

#### Scenario: Steelman defeats conclusion
- **WHEN** the strongest opposing case defeats or materially undercuts the preferred conclusion
- **THEN** LogicGuard routes the claim to downgrade, omission, further source discovery, or explicit unresolved status

### Requirement: Internal Atlas And Reader Artifact Separation
The system SHALL separate the internal Atlas from the reader-facing artifact. The final artifact MUST remain genre-appropriate and readable while preserving Atlas outputs in an appendix, support material, or local run record when useful.

#### Scenario: Atlas is too detailed for final prose
- **WHEN** the full Atlas would make the user-facing report read like a diagnostic dump
- **THEN** the final artifact presents the conclusion and important limitations cleanly while keeping detailed branch, debate, lens, expert, trace, and tournament material in support sections

### Requirement: Generic Validation Across Domains
The upgrade SHALL be validated against multiple unrelated topic classes or generic fixtures. A rule that only works for one domain MUST NOT be treated as a core skill rule.

#### Scenario: Multi-domain regression
- **WHEN** the upgraded skill guidance is validated
- **THEN** checks include at least several different topic classes or abstract fixtures that cover policy, technical, organizational, scientific, market, or social research patterns without relying on one domain's vocabulary
