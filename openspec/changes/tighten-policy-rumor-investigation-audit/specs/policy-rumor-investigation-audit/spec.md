## ADDED Requirements

### Requirement: Policy rumor investigations separate evidence roles
The workflow SHALL separate policy-rumor and current-event evidence into trigger claim, official action, jurisdiction/scope, implementation evidence, market or execution data, fiscal or motive context, expert commentary, and future hypothesis before writing a confident conclusion.

#### Scenario: Local pilot action is not national implementation
- **WHEN** an investigation finds a local pilot policy and a broader national rumor
- **THEN** the workflow records the local pilot action separately from any national implementation claim and does not treat the local action as national rollout evidence without additional official implementation sources

#### Scenario: Fiscal pressure is motive context
- **WHEN** sources show fiscal pressure or expert arguments for a policy
- **THEN** the workflow labels those sources as motive/context or expert analysis and does not treat them as implementation evidence

### Requirement: Negative or partial findings show checked implementation signals
The workflow SHALL list which implementation signals were checked or missing before concluding that a policy rollout is unsupported, partial, or only hypothetical.

#### Scenario: No implementation details found
- **WHEN** no implementation details are found for an alleged policy rollout
- **THEN** the report names the missing signals such as official implementing rule, jurisdiction list, tax rate or standard, effective date, enforcement guidance, budget treatment, or execution data

### Requirement: Reports include a reader route and handoffs
Substantive reports SHALL include a reader route or equivalent early orientation and SHALL preserve section handoffs and paragraph jobs in the writing plan before final prose.

#### Scenario: Long report synthesis
- **WHEN** a report has multiple evidence chains, competing interpretations, or future projections
- **THEN** the workflow defines the section order, why each section follows the prior section, what each core paragraph proves or limits, and where source markers belong

### Requirement: Source markers carry role, freshness, and claim use
The workflow SHALL attach each important source marker to source role, date or freshness, claim use, and limitation where relevant; a bibliography alone SHALL NOT count as support for important source-backed claims.

#### Scenario: Source used for expert analysis
- **WHEN** a source is used for expert analysis rather than official action
- **THEN** the claim-to-source matrix and final prose label that role and avoid presenting the expert view as policy execution evidence

### Requirement: Closure validates privacy and installed-source parity
Before claiming the upgraded skill work is complete, the workflow SHALL verify local/private investigation artifacts remain ignored, changed skill sources are synced to installed Codex skill folders, and only software/skill-source changes are committed.

#### Scenario: Skill source was edited
- **WHEN** a project-local skill source changes
- **THEN** the installed skill copy is updated, parity is checked, and the local Git commit excludes investigation reports, private ledgers, TraceGuard cases, and LogicGuard source libraries
