## ADDED Requirements

### Requirement: Source Portfolio Coverage
The research workflow SHALL require a source portfolio plan for substantive investigations, covering primary or closest-available records, official or regulatory records when relevant, execution or outcome records, independent or third-party records, expert or model sources when interpretation matters, counter or limiting sources, source-lineage checks, and future-trigger sources.

#### Scenario: High-value source class missing
- **WHEN** a substantive investigation reaches final drafting with a missing required source class
- **THEN** the workflow MUST either route a targeted SourceGuard search action or visibly downgrade the dependent claim.

### Requirement: Key Claim And Number Ledger
The research workflow SHALL maintain a key-claim and key-number ledger for material figures, quantified claims, and central conclusions. Each ledger entry MUST include source id, source date or coverage period, source role, claim type, support boundary, unsupported overclaim wording, final treatment, and required citation marker.

#### Scenario: Forecast number written as observed fact
- **WHEN** a key-number ledger entry marks a figure as forecast, model estimate, announcement, or scenario
- **THEN** final prose MUST NOT write that figure as already observed unless a separate observed-fact source supports it.

### Requirement: Transmission And Effect Chain
For causal, market-effect, price-effect, policy-effect, adoption, execution, outcome, or impact claims, the workflow SHALL require an explicit transmission or effect chain that separates cause, mechanism, intermediate signal, outcome, stakeholder signal, counter or limiting evidence, and future trigger.

#### Scenario: Intermediate market signal lacks final outcome evidence
- **WHEN** a chain supports an intermediate signal but lacks final outcome or stakeholder evidence
- **THEN** the final claim MUST be qualified to the supported chain layer.

### Requirement: Hierarchical TraceGuard Modeling
TraceGuard use in substantive investigations SHALL model important leads in layers: lead, event fact, explanation hypothesis, outcome or impact claim, execution chain, competing storyline, causal chain, counterfactual question, confounder ledger, gap, and safe wording.

#### Scenario: Smooth storyline hides live alternative
- **WHEN** evidence leaves a material alternative explanation live
- **THEN** TraceGuard handoff MUST preserve the competing storyline and safe wording rather than collapsing to one clean narrative.

### Requirement: Hierarchical LogicGuard Modeling
LogicGuard use for substantive final artifacts SHALL model the artifact at the user-requested genre's natural levels, such as document to section to paragraph, deck to section to slide, paper to section to paragraph, or memo to decision block. High-importance artifact units MUST expose local claim, evidence, warrant, assumption, limitation, rebuttal or undercutter, source role, and final treatment.

#### Scenario: Core paragraph has citation but unsupported scope
- **WHEN** a core artifact unit cites a source whose role or scope does not support the unit's exact claim wording
- **THEN** LogicGuard MUST flag semantic source-fit risk and require search, weakening, relocation, or omission.

### Requirement: Genre-Adaptive Final Artifact Review
Final artifact review SHALL evaluate whether the output fits the user-requested artifact genre and audience, not a fixed report style. The workflow MUST preserve requested formats such as report, paper, memo, article, literature review, deck storyline, or decision note.

#### Scenario: User requests paper-style output
- **WHEN** the user requests a paper-style artifact rather than a report
- **THEN** LogicGuard and the research workflow MUST review structure, evidence placement, limitations, and citations against that paper-style target instead of forcing an executive-report layout.

### Requirement: Helper Checks
The research workflow SHALL provide lightweight helper checks for source portfolio ledgers, key-claim ledgers, and claim/source semantic-fit risk, alongside existing Markdown citation and source-role coverage checks.

#### Scenario: Helper detects blocked semantic fit
- **WHEN** a helper reports a hard mismatch such as national-scope wording supported only by regional evidence, execution wording supported only by announcement evidence, or observed-fact wording supported only by forecast evidence
- **THEN** closure MUST be blocked or downgraded until the artifact is repaired or the warning is explicitly scoped.

### Requirement: Install And Repository Sync
The upgrade SHALL keep source repository files and installed Codex skill folders synchronized for the touched skills, while preserving peer-agent changes and avoiding FlowGuard behavior changes.

#### Scenario: Installed skill differs from source after edits
- **WHEN** a touched installed skill file differs from the source repository counterpart after validation
- **THEN** the sync step MUST report the difference and repair or explicitly scope the closure before claiming the upgrade complete.
