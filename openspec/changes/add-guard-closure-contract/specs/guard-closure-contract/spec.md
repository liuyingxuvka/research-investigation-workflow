## ADDED Requirements

### Requirement: Research closure aggregates helper evidence
The research workflow SHALL provide an aggregate closure report that includes citation marker hygiene, source-role coverage, source portfolio, key-claim ledger, semantic source-fit, stale evidence, skipped checks, and next actions.

#### Scenario: Citation helper fails
- **WHEN** the Markdown source marker helper reports undefined or duplicate source markers
- **THEN** the aggregate closure report is blocked and recommends repair or downgrade before final delivery

### Requirement: Stale final artifact blocks full research closure
The research workflow SHALL mark closure evidence stale when the final artifact changes after citation, source-fit, or LogicGuard audit.

#### Scenario: Final artifact changed after audit
- **WHEN** the research ledger says final artifact status is stale after edit
- **THEN** the aggregate closure report is non-passing and routes back to freshness validation
