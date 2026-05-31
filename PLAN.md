# Research Investigation Workflow Plan

## 1. Goal

Create a Codex skill named `research-investigation-workflow`.

The skill coordinates full research and investigation runs from a user topic to
a final readable report, while keeping evidence, gaps, assumptions, and process
closure explicit.

Plain version:

```text
The skill helps AI investigate a topic step by step, remember what it has
already checked, organize evidence into a story, find missing links, search
again, write a human-readable report, audit the report, and record the run for
future reuse.
```

## 2. Existing Capabilities To Reuse

This skill should be built on existing workflows, not from scratch.

### TraceGuard

Use TraceGuard for:

- saving messy investigation material by case and direction;
- separating source, evidence, event, trace, gap, and contradiction;
- building evidence-backed event timelines and storylines;
- detecting missing evidence, weak links, contradictions, and unsafe claim
  boundaries;
- exporting LogicGuard-ready claim bundles when final writing starts.

TraceGuard pipeline:

```text
source -> evidence -> event -> trace/storyline -> gap ledger -> contradiction ledger -> claim boundary
```

### LogicGuard

Use LogicGuard for:

- preserving important formal sources in the source library;
- modeling claims, evidence, warrants, assumptions, rebuttals, limitations, and
  scope;
- deepening weak or important claims;
- generating target story plans, outlines, report structures, and paragraph
  blueprints;
- creating the final human-readable report;
- auditing whether final claims are structurally supported.

LogicGuard pipeline:

```text
source library -> argument model -> gaps/diagnostics -> artifact synthesis -> final claim audit
```

### FlowGuard

Use FlowGuard for:

- keeping the investigation workflow in the right order;
- tracking which artifacts changed after which validation;
- preventing stale evidence from being treated as current;
- requiring rechecks after new evidence or major prose changes;
- deciding whether the run can honestly claim completion.

FlowGuard pipeline:

```text
stage order -> artifact versions -> validation evidence -> stale-evidence review -> closure
```

## 3. Four Memory Layers

The skill must keep four memory layers separate.

### 3.1 TraceGuard Case Library

Purpose:

```text
case-scoped investigation memory
```

Stores:

- sources;
- extracted evidence;
- events;
- traces and storylines;
- gaps;
- contradictions;
- search tasks;
- direction notes.

Use when material is messy, incomplete, temporary, or case-specific.

### 3.2 LogicGuard Source Library

Purpose:

```text
durable source support for final arguments, reports, papers, and reusable reasoning
```

Stores:

- formal sources;
- shallow and deep source models;
- project source branches;
- source-node links;
- important evidence paths.

Use only when a source is stable, important, and worth formal preservation.

### 3.3 FlowGuard Logs And Process Evidence

Purpose:

```text
workflow evidence and closure safety
```

Stores or checks:

- process stages;
- validations;
- stale evidence;
- revalidation requirements;
- completion boundaries.

Use to prevent the AI from saying the investigation is complete when a later
change has made old checks stale.

### 3.4 Research Investigation History Ledger

Purpose:

```text
cross-run memory of how investigations were performed
```

This is the user's new requirement. It does not store evidence as truth. It
stores reusable workflow memory.

Stores:

- investigation topic;
- user goal and report type;
- evidence access policy;
- search directions used;
- useful search terms;
- failed search directions;
- TraceGuard case references;
- LogicGuard source/model references;
- final report references;
- unresolved gaps;
- reusable lessons;
- FlowGuard closure status.

Use this at the start and end of every investigation.

## 4. Full Workflow

### Stage 0: History Preflight

Before starting a new investigation, search the Research Investigation History
Ledger.

Questions:

- Have we investigated a similar topic before?
- Did a prior run use useful search directions?
- Are there existing TraceGuard cases to reuse?
- Are there existing LogicGuard sources or models to reuse?
- Were there unresolved gaps that matter now?

Output:

```text
prior_run_matches
reusable_search_directions
reusable_artifacts
known_gaps
```

### Stage 1: User Goal Intake

Clarify:

- topic;
- target audience;
- desired report type;
- desired conclusion strength;
- public search permission;
- local or internal search permission;
- time budget or depth;
- output length and style.

Conclusion strength levels:

```text
initial leads
working hypothesis
evidence-backed finding
deep research conclusion
formal report / paper-grade conclusion
```

### Stage 2: Evidence Source Policy

Classify possible evidence sources:

```text
public evidence
local evidence
internal evidence
permission-gated evidence
hypothesis / inference
```

Rules:

- Public evidence can be searched online when allowed.
- Local or internal evidence requires user access and available tools.
- Permission-gated evidence becomes an access gap.
- Hypothesis is allowed, but must be labeled as hypothesis.
- No hypothesis can be written as evidence.

### Stage 3: First-Round Search

Search along several directions:

- timeline;
- actors;
- location;
- cause;
- impact;
- contradiction;
- missing proof;
- follow-up consequences;
- public record;
- internal record.

Each found item should be saved as a source first, not as a conclusion.

### Stage 4: Save To TraceGuard Case Library

Create or reuse:

```text
case -> direction -> source -> evidence -> event -> trace
```

Rules:

- A source is not evidence by itself.
- Evidence is not an event by itself.
- A trace is not a final claim by itself.
- Weak signals remain weak signals.
- Access gaps stay visible.

### Stage 5: Build And Evaluate TraceGuard Model

Use TraceGuard to:

- build a model from case material;
- validate schema and hard gates;
- evaluate storyline support;
- diagnose contradictions;
- generate gap ledger;
- produce safe and unsafe wording guidance.

Output:

```text
storyline candidates
validated / candidate / weak / contradicted status
timeline
gaps
contradictions
claim boundaries
suggested next evidence
```

### Stage 6: Gap-Driven Search Loop

For each important gap, decide the next route:

```text
missing public evidence -> public search
missing local evidence -> local file / Drive / notes / logs search if allowed
missing internal evidence -> internal source search if allowed
missing source permission -> access gap
missing warrant or explanation -> LogicGuard model gap
conflicting evidence -> TraceGuard contradiction review
```

Loop:

```text
search -> save -> extract evidence -> rebuild TraceGuard model -> re-evaluate -> write gaps back
```

Stop only when:

- the target conclusion level is met;
- the user budget is reached;
- critical evidence is inaccessible;
- remaining gaps are explicitly accepted;
- the claim is downgraded to match evidence.

### Stage 7: Promote Stable Sources To LogicGuard

Only promote selected material from TraceGuard to LogicGuard when it is:

- important to the final claim;
- stable enough to preserve formally;
- useful for future reports or papers;
- not merely a temporary clue or rejected search result.

Promotion is explicit. TraceGuard Case Library and LogicGuard Source Library
must remain separate.

### Stage 8: LogicGuard Argument Modeling And Deepening

Use LogicGuard to model:

- root claims;
- supporting evidence;
- warrants or mechanisms;
- assumptions;
- rebuttals;
- limitations;
- scope;
- missing support.

Deepen high-importance or weak nodes before writing confident prose.

### Stage 9: LogicGuard Artifact Synthesis

Generate a target story plan before final prose.

Possible output profiles:

```text
news-style article
research report
internal briefing
incident review
policy memo
paper-style long report
executive summary
```

The final answer should have two layers:

1. Human-readable report.
2. Evidence and audit appendix.

The main report should not look like a machine diagnostic dump.

### Stage 10: LogicGuard Final Claim Audit

Audit the written report for:

- overclaiming;
- missing warrant;
- hidden assumption;
- unsupported causality;
- scope mismatch;
- unanswered rebuttal;
- missing limitation;
- candidate written as confirmed;
- hypothesis written as evidence.

If audit fails:

```text
either search for more evidence
or weaken the claim
or move the claim to hypothesis / unresolved section
```

### Stage 11: FlowGuard Closure

Use FlowGuard to check:

- stages ran in the intended order;
- new evidence did not stale old conclusions;
- model checks were rerun after major changes;
- final prose was audited after writing;
- closure status is supported by current evidence.

Do not claim completion from stale checks.

### Stage 12: Final Delivery

Deliver:

- readable main report;
- executive summary;
- timeline or storyline;
- key findings;
- confidence and evidence levels;
- hypothesis and assumption ledger;
- unresolved gaps;
- source appendix;
- TraceGuard summary;
- LogicGuard audit summary;
- FlowGuard closure summary.

### Stage 13: History Postflight

Write the run back to the Research Investigation History Ledger.

Record:

- what was investigated;
- what worked;
- what failed;
- what sources or models were reused;
- which gaps remained;
- where final artifacts are;
- what future similar runs should try first.

## 5. First-Version Implementation Scope

First version should create a Codex skill, not a full app.

Recommended skill layout:

```text
research-investigation-workflow/
  SKILL.md
  agents/
    openai.yaml
  references/
    workflow.md
    evidence-source-policy.md
    traceguard-loop.md
    logicguard-report-synthesis.md
    flowguard-closure.md
    history-ledger.md
    output-contract.md
```

Avoid scripts in the first pass unless a repeated file operation becomes
fragile. The existing TraceGuard and LogicGuard CLIs already cover the first
implementation.

## 6. Acceptance Criteria

The first implementation is acceptable when:

- the skill triggers for research, investigation, evidence collection, report
  synthesis, and Guard-family orchestration requests;
- it starts with history preflight;
- it distinguishes public, local, internal, access-gated, and hypothetical
  information;
- it routes messy evidence to TraceGuard Case Library;
- it routes formal sources to LogicGuard Source Library only by explicit
  promotion;
- it uses TraceGuard gaps to drive more searching;
- it uses LogicGuard to synthesize a human-readable report and audit final
  claims;
- it uses FlowGuard for staged process and stale-evidence closure;
- it writes a history postflight record;
- it does not claim factual certainty from confidence scores;
- it keeps final prose separate from audit appendices.

