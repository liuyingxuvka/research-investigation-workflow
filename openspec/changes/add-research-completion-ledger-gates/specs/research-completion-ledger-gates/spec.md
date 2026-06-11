## ADDED Requirements

### Requirement: Research completion ledger rows
The research workflow SHALL keep top-level completion ledger rows for each
important child Guard route used or intentionally skipped in a substantive
investigation.

#### Scenario: Child Guard route is used
- **WHEN** SourceGuard, TraceGuard, LogicGuard, or FlowGuard contributes to a
  research run
- **THEN** the research ledger records its status, evidence, stale evidence,
  skipped checks, safe claim, unsafe claim boundary, and next action

#### Scenario: Child Guard route is skipped
- **WHEN** a normally relevant child Guard route is skipped
- **THEN** the research ledger records the skip reason and downgrades closure
  when the skip weakens the requested claim

### Requirement: Weakest important row governs final claim
The research workflow SHALL match final claim strength to the weakest important
unresolved evidence row.

#### Scenario: Source evidence is partial
- **WHEN** a central claim depends on a partial source row
- **THEN** the final artifact cannot state that claim with full confidence
