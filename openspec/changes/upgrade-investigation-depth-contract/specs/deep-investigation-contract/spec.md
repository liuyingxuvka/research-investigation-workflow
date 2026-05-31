## ADDED Requirements

### Requirement: Default deep investigation by logic leads
The skill SHALL treat substantive investigation requests as deep, logic-lead-driven investigations by default. It MUST NOT use source-count thresholds or shallow/medium/deep modes as the primary measure of research depth.

#### Scenario: User asks for a detailed investigation
- **WHEN** a user asks for a research report, investigation, or detailed explanation of an event
- **THEN** the workflow starts by identifying major logic leads and evidence chains rather than asking how many sources to collect

### Requirement: Logic-lead map before final writing
The skill SHALL create or maintain a logic-lead map before final prose. Each important lead MUST record the question or hypothesis, supporting evidence, counter or support-limiting evidence, unresolved gaps, current claim strength, and report eligibility.

#### Scenario: Important motive lead has weak support
- **WHEN** a motive, cause, actor-interest, outcome, contradiction, or future-impact lead lacks support or has only one-sided support
- **THEN** the lead remains a gap, hypothesis, or downgraded claim rather than being written as a finding

### Requirement: TraceGuard evidence-chain handoff
TraceGuard usage SHALL produce investigation handoff material containing event chains, explanation leads, evidence-chain status, contradictions, gaps, safe wording, and follow-up search directions for important unresolved leads.

#### Scenario: Event fact and explanation differ
- **WHEN** a source confirms that an event happened but does not prove the motive or effect
- **THEN** TraceGuard handoff separates the event fact from the explanation lead and marks the explanation with its own support status

### Requirement: LogicGuard citation-grounded report synthesis
LogicGuard usage SHALL require a claim-to-source matrix, section blueprint, paragraph blueprint, and inline citation markers for important report claims. Each important factual claim, official-claim report, analytic inference, limitation, and future hypothesis MUST identify its source role.

#### Scenario: A paragraph combines official claims and limiting evidence
- **WHEN** report prose states an official outcome claim and a third-party limitation
- **THEN** the paragraph includes inline citation markers for both source roles and labels the resulting conclusion with the appropriate claim strength

### Requirement: Final prose audit after last material change
The workflow SHALL run or perform a LogicGuard final claim audit after the last material report edit. The audit MUST check unsupported claims, missing inline citations, missing warrants, overclaiming, hidden assumptions, unanswered rebuttals, missing limitations, and candidate claims written as findings.

#### Scenario: Report text changes after audit
- **WHEN** final report prose changes after a LogicGuard audit
- **THEN** prior audit evidence is stale and the workflow reruns the audit or marks closure partial

### Requirement: FlowGuard closure remains orchestration-specific
The workflow SHALL use FlowGuard for stage order, evidence freshness, stale checks, validation coverage, local-output privacy, and honest completion claims. It MUST NOT require changing the standalone FlowGuard skill to enforce research-report content rules.

#### Scenario: Investigation outputs are produced in a software repository
- **WHEN** reports, TraceGuard cases, LogicGuard source libraries, or History Ledger records are generated during a skill run
- **THEN** closure verifies they remain local-only or ignored unless the user explicitly requests a sanitized published sample

### Requirement: Software-only Git sync
Every upgraded skill SHALL be synchronized across its installed copy and local source mirror when both exist. Git commits SHALL include only software/skill source and public documentation changes, not generated investigation run outputs.

#### Scenario: Installed skill has a local Git source mirror
- **WHEN** a skill is updated in an installed folder and a local Git source mirror exists
- **THEN** the same source changes are applied to the mirror, validated, and committed without including ignored local run artifacts
