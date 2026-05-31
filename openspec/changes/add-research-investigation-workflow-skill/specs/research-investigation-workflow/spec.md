## ADDED Requirements

### Requirement: Skill trigger and first steps
The skill SHALL trigger for multi-round research, investigation, evidence collection, report synthesis, and Guard-family orchestration requests. It MUST begin with Research Investigation History Ledger preflight, evidence-source policy classification, and route selection across TraceGuard, LogicGuard, and FlowGuard.

#### Scenario: New investigation request
- **WHEN** a user asks Codex to investigate a topic and produce a report
- **THEN** the skill starts from history preflight, classifies allowed evidence sources, and selects the Guard-family workflow routes before claiming findings

### Requirement: Guard-family boundary separation
The skill SHALL keep TraceGuard Case Library, LogicGuard Source Library, FlowGuard process evidence, and Research Investigation History Ledger as separate memory layers. It MUST NOT merge the TraceGuard Case Library and LogicGuard Source Library or treat History Ledger records as factual proof.

#### Scenario: Prior run contains related artifacts
- **WHEN** the History Ledger has a similar prior investigation
- **THEN** the skill returns reusable workflow guidance and artifact pointers without silently importing prior evidence as truth

### Requirement: Evidence source policy
The skill SHALL classify information as public evidence, local evidence, internal evidence, permission-gated evidence, or hypothesis/inference. It MUST label access gaps and hypotheses clearly, and MUST NOT write hypotheses as evidence.

#### Scenario: Source access is unavailable
- **WHEN** an important source requires permission or unavailable internal access
- **THEN** the skill records an access gap and downgrades or delays claims that depend on that source

### Requirement: TraceGuard investigation loop
The skill SHALL use TraceGuard for messy case material, evidence extraction, event and trace building, gap ledgers, contradiction review, and claim-boundary guidance. TraceGuard gaps MUST drive additional search loops when the requested conclusion strength requires more support.

#### Scenario: TraceGuard finds an important gap
- **WHEN** TraceGuard evaluation returns a gap that affects the requested conclusion strength
- **THEN** the skill routes the gap to public, local, internal, access-gap, LogicGuard-warrant, or contradiction follow-up before finalizing

### Requirement: LogicGuard report synthesis and audit
The skill SHALL promote only selected stable and important sources from TraceGuard into LogicGuard formal source workflows. It MUST use LogicGuard to model support, deepen weak or important claims, synthesize a human-readable report, and audit final claims before delivery.

#### Scenario: Final prose contains a strong causal claim
- **WHEN** the report draft contains a causal or high-confidence claim
- **THEN** the skill audits the claim with LogicGuard for support, warrants, assumptions, rebuttals, limitations, and scope before presenting it as a finding

### Requirement: FlowGuard closure
The skill SHALL use FlowGuard to track stage order, artifact versions, validation evidence, stale checks, minimum revalidation, and closure status. It MUST NOT claim completion from stale, skipped, failed, or progress-only evidence.

#### Scenario: New evidence arrives after report synthesis
- **WHEN** new evidence or major prose changes occur after an earlier model check
- **THEN** the skill identifies stale evidence and reruns the minimum required checks before closure

### Requirement: History Ledger postflight
The skill SHALL write a Research Investigation History Ledger record at the end of each investigation run unless blocked by missing storage access. The record MUST include topic, goal, evidence policy, useful and failed search directions, linked Guard-family artifacts, unresolved gaps, reusable lessons, privacy labels, and FlowGuard closure status.

#### Scenario: Investigation ends with unresolved gaps
- **WHEN** the investigation closes with accepted or unavoidable gaps
- **THEN** the skill records those gaps in the History Ledger and reflects the downgraded conclusion strength in final delivery

### Requirement: Output contract
The skill SHALL deliver a human-readable main report plus evidence and audit appendix material. It MUST separate findings from hypotheses, assumptions, limitations, unresolved gaps, source appendix, TraceGuard summary, LogicGuard audit summary, and FlowGuard closure summary.

#### Scenario: User requests a research report
- **WHEN** the user asks for a final research report
- **THEN** the skill produces readable prose for the main report and keeps diagnostic details in appendix or summary sections
