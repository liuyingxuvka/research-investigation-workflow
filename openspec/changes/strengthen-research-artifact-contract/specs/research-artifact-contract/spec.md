## ADDED Requirements

### Requirement: Research Plan Card
For substantive investigation work, the workflow SHALL create a lightweight research plan card before broad search or final artifact drafting.

#### Scenario: Substantive investigation starts
- **WHEN** Codex uses `research-investigation-workflow` for a substantive investigation
- **THEN** it records the research question, target claim strength, key leads, priority source types, required counter or limiting evidence, downgrade rule, and requested final artifact genre before broad search

### Requirement: Per-Round Replanning Gate
After each meaningful source search or source-reading batch, the workflow SHALL choose and record the next research move before drafting final claims.

#### Scenario: Search batch completes
- **WHEN** a meaningful batch finds sources, contradictions, gaps, or access limits
- **THEN** the workflow chooses whether to deepen the same lead, switch source type, seek counter evidence, seek execution evidence, refresh recency, route to TraceGuard, route to LogicGuard, downgrade the claim, or stop with an explicit gap

### Requirement: Source Search Tactics
The workflow SHALL guide SourceGuard to consider reusable search tactics appropriate to each important lead without treating SourceGuard as a crawler or truth oracle.

#### Scenario: Important lead needs source discovery
- **WHEN** an important lead lacks sufficient source coverage
- **THEN** the workflow considers original-source, specific-site, source-lineage, independent-source, counter/limiting, execution/outcome, freshness, stakeholder, absence-signal, or multimodal-anchor tactics as applicable

### Requirement: Source Reading Observations
The workflow SHALL record what a found source can and cannot support before promoting it downstream.

#### Scenario: Candidate source is found
- **WHEN** a candidate source is found or read
- **THEN** the observation records what the source says, what it can support, what it cannot support, source role, source date or freshness, locator, contradiction or limitation, new leads, and handoff readiness where available

### Requirement: Event Explanation Outcome Separation
The workflow SHALL keep event facts, explanations, and outcomes distinct during TraceGuard handoff and final artifact planning.

#### Scenario: Evidence supports only one claim layer
- **WHEN** evidence supports an event fact but not the explanation or outcome
- **THEN** TraceGuard guidance keeps the explanation or outcome as candidate, weak, access-gap, not-supported, or downgraded rather than allowing it to become a confirmed finding

### Requirement: Genre-Preserving Final Artifact
The workflow SHALL preserve the user's requested final artifact genre while enforcing support coverage behind the artifact.

#### Scenario: User requests a non-report artifact
- **WHEN** the user requests a paper, brief, memo, article, deck storyline, or other research-backed artifact
- **THEN** the final artifact follows that genre and does not become a Guard-family tool log or fixed diagnostic checklist

### Requirement: Claim-To-Prose Mapping
Before final artifact drafting, important claims SHALL be mapped to their target prose or artifact location with support metadata.

#### Scenario: Important claim enters final artifact
- **WHEN** an important claim is included in the final artifact
- **THEN** it maps to a paragraph, sentence, page, slide, section, or other artifact locator with source ids, source role, claim use, limitation or rebuttal where relevant, and final treatment

### Requirement: Material Limits Must Surface
Material limits, contradictions, and unresolved gaps SHALL be covered in the final artifact where they affect interpretation, without forcing them into fixed visible headings.

#### Scenario: Limitation affects main conclusion
- **WHEN** a limitation, contradiction, or gap materially changes claim strength
- **THEN** the final artifact covers it in genre-appropriate prose, notes, tables, or appendix, and the claim is downgraded if support remains insufficient
