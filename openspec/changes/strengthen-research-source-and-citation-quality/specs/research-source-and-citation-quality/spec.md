## ADDED Requirements

### Requirement: Source registry for substantive artifacts
The research workflow SHALL maintain a source registry for every substantive source-backed investigation artifact. The registry MUST preserve source id, title, publisher or owner when known, source date or freshness clue, coverage period when known, URL or locator, source role, support boundary, cannot-support boundary, promotion status, and final citation marker.

#### Scenario: Source is promoted from discovery to final support
- **WHEN** a candidate source becomes important to a final claim
- **THEN** the source registry records why it was promoted, what role it fills, what it supports, what it cannot support, and which final marker such as `[S1]` identifies it

#### Scenario: Source is not ready for citation
- **WHEN** a source is only a search hit, snippet, duplicate, weak signal, permission gap, or unread candidate
- **THEN** the source registry marks it as not citation-ready and the final artifact must not use it as direct support

### Requirement: Source-role coverage review
SourceGuard SHALL produce or update a source-role coverage review for substantive investigations. The review MUST classify original/direct facts, source statements, independent corroboration, scope boundaries, execution/outcome evidence, context/motive evidence, expert interpretation, counter/limiting evidence, stakeholder evidence, freshness/current-state evidence, and future-trigger evidence as found, read, anchored, blocked, not applicable, or gap.

#### Scenario: Important source role remains missing
- **WHEN** a source role is material to the requested conclusion and remains gap or blocked
- **THEN** the research workflow must either route the gap back through SourceGuard, mark an access or evidence gap, or downgrade the affected claim

#### Scenario: Post-draft source gap review finds a missing high-value source class
- **WHEN** the draft artifact makes a material claim without a regulator, primary record, execution record, independent report, counter source, or freshness source that should reasonably exist
- **THEN** SourceGuard must recommend a targeted follow-up search or the final claim must be weakened

### Requirement: Execution-chain status for important leads
TraceGuard SHALL track the execution-chain status for each important lead where announcements, plans, forecasts, contracts, operations, outcomes, or market effects can be confused. The status MUST distinguish announcement, approval, contract or financial commitment, construction or implementation, commercial operation or actual use, market or system result, end-user outcome, contradiction, access gap, and not supported when applicable.

#### Scenario: Announcement is mistaken for execution
- **WHEN** available evidence supports only an announcement, proposal, queue request, forecast, or company statement
- **THEN** TraceGuard must mark execution evidence as missing and provide safe wording that prevents final prose from treating the claim as implemented or outcome-proven

#### Scenario: Execution evidence exists but outcome evidence is missing
- **WHEN** a project, policy, or market change has implementation evidence but no supported outcome or impact evidence
- **THEN** TraceGuard must allow qualified execution wording but block or downgrade outcome wording

### Requirement: Citation consistency and claim-source audit
LogicGuard SHALL require citation consistency and claim-source audit before a substantive final artifact is marked complete. The audit MUST check inline marker definitions, unused or undefined source ids, source-role mismatch, important claims without inline markers, official claims written as independent facts, prediction written as fact, and stale audit after material prose changes.

#### Scenario: Undefined or mismatched citation marker exists
- **WHEN** final prose uses a marker such as `[S19]` that is not defined, points to a different source than the claim needs, or is materially inconsistent with the source registry
- **THEN** the artifact must fail the citation gate until the marker, registry, or prose is corrected

#### Scenario: Final prose changes after audit
- **WHEN** material source-backed prose changes after citation audit
- **THEN** the prior audit is stale and must be rerun or the closure must be marked partial

### Requirement: Final research quality gate
The research workflow SHALL run a final quality gate before delivering a substantive source-backed investigation artifact. The gate MUST summarize source-role coverage, execution-chain coverage, citation audit status, claim strength, skipped checks, and unresolved gaps.

#### Scenario: All gates pass
- **WHEN** source-role coverage, execution-chain review, and citation audit support the requested conclusion strength
- **THEN** the workflow may deliver the artifact with the corresponding claim strength and a concise closure statement

#### Scenario: A gate fails or is skipped
- **WHEN** a material source-role, execution-chain, or citation audit gate fails or is skipped
- **THEN** the final artifact must be labeled partial, downgraded, initial, or blocked, and must state what evidence or repair remains necessary

### Requirement: Installed and source skill synchronization
Every changed skill SHALL be synchronized between its source repository or project-local copy and the installed Codex skill folder before the task is marked complete.

#### Scenario: Source skill changes
- **WHEN** a source skill or project-local skill file is changed
- **THEN** the matching installed skill file must be updated or the final status must explain why synchronization was blocked

#### Scenario: Installed skill validation
- **WHEN** installed skill files are synchronized
- **THEN** the skill folder must pass available quick validation or the final status must report the validation failure and affected skill
