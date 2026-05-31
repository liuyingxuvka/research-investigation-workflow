## ADDED Requirements

### Requirement: SourceGuard plans first-round discovery
For substantive investigation runs, the workflow SHALL build or update a SourceGuard belief state before executing broad evidence search.

#### Scenario: Heavy investigation begins
- **WHEN** a user asks for a substantive investigation, report, evidence collection, or claim audit
- **THEN** the workflow records leads, candidate source roles, gaps, source policy, and next search actions in SourceGuard before first-round search

#### Scenario: Small non-investigation answer
- **WHEN** the task is a short direct answer with no evidence-discovery loop
- **THEN** the workflow may skip SourceGuard and state that the heavy investigation route was not used

### Requirement: SourceGuard separates source access classes
The workflow SHALL classify planned and observed material as public, local, internal, permission-gated, or hypothesis/inference before treating it as usable evidence.

#### Scenario: Permission-gated candidate
- **WHEN** a plausible source requires credentials, subscription, legal permission, or unavailable access
- **THEN** SourceGuard records an access gap and the workflow does not cite that material as support

#### Scenario: Local or internal source allowed
- **WHEN** the user has allowed local or internal search and a connected tool or path is available
- **THEN** SourceGuard may plan the search action, but observations must preserve source role, locator, privacy label, and extraction method

### Requirement: SourceGuard receives TraceGuard gaps
The workflow SHALL route important TraceGuard gaps back into SourceGuard as search-action planning input.

#### Scenario: Execution evidence missing
- **WHEN** TraceGuard finds a claimed outcome without implementation, operating, transaction, stakeholder, or follow-up evidence
- **THEN** SourceGuard plans execution-focused searches such as primary records, procurement, local reports, images, videos, report pages, or other concrete signals

#### Scenario: One-sided evidence
- **WHEN** TraceGuard finds only official, actor, or hypothesis-supporting material
- **THEN** SourceGuard plans independent, counter, and limiting-source searches before strong claim wording is allowed

### Requirement: SourceGuard preserves observations before promotion
The workflow SHALL record found material as SourceGuard observations before TraceGuard event modeling or LogicGuard formal promotion.

#### Scenario: Search finds a candidate source
- **WHEN** public, local, or internal search finds a source
- **THEN** the workflow records it as a candidate source with source role, access status, date/freshness, and notes rather than treating it as final evidence

#### Scenario: Search finds multimodal material
- **WHEN** search finds PDF pages, book pages, images, videos, audio, tables, maps, or citations
- **THEN** the workflow records locator-aware anchors and does not invent OCR, transcripts, visual recognition, or audio content

### Requirement: LogicGuard receives selected candidates only
The workflow SHALL promote only stable, important SourceGuard/TraceGuard-selected candidates into LogicGuard.

#### Scenario: Raw search results exist
- **WHEN** a search produces many weak, duplicate, irrelevant, or unanchored sources
- **THEN** the workflow does not bulk-promote them into LogicGuard

#### Scenario: Candidate source supports final report
- **WHEN** a source is important to a final claim and has a clear role, date/freshness, anchor or limitation, and claim-use label
- **THEN** it may be promoted into LogicGuard for source preservation, claim-to-source matrix work, and final audit

### Requirement: Output wording preserves SourceGuard boundaries
The workflow SHALL prevent SourceGuard scores, search hits, or candidate sources from being written as factual confidence.

#### Scenario: High SourceGuard score
- **WHEN** a search action receives a high expected utility score
- **THEN** the report may say the action is valuable for closing a source gap, but must not say the claim is likely true because of that score

#### Scenario: Final closure has unresolved SourceGuard gaps
- **WHEN** critical SourceGuard gaps remain open, blocked, permission-gated, stale, or contradicted
- **THEN** the workflow downgrades the conclusion strength or labels the output as an initial/staged/qualified investigation
