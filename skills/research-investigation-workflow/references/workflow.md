# End-To-End Workflow

Use this file for the default investigation route. This skill defaults to deep, logic-lead-driven investigation. Keep the work staged, and show when evidence, claims, or validation are partial.

## Stage 0: History Preflight

Search `.research-investigation-history/index.yaml` and run summaries for similar topics, entities, report types, evidence policies, and useful search directions.

Return only:

- prior run matches;
- reusable search directions;
- reusable artifact pointers;
- known unresolved gaps;
- privacy or permission constraints.

Do not import old evidence as truth.

## Stage 1: Goal Intake

Identify:

- topic and scope;
- target audience;
- requested final artifact genre, such as report, paper, memo, brief, article, literature review, deck storyline, decision note, or another user-requested format;
- desired conclusion strength;
- public, local, and internal search permissions;
- time or depth budget;
- output length and tone.
- important actors, motives, event facts, outcomes, contradictions, limiting evidence, follow-up consequences, and alternative explanations that may become logic leads.

Conclusion strength levels:

```text
initial leads
working hypothesis
evidence-backed finding
deep research conclusion
formal report / paper-grade conclusion
```

If the user has not specified a conclusion strength, default to `working hypothesis` for a quick pass and `evidence-backed finding` for a substantive final artifact request.

Do not ask the user to choose a shallow/medium/deep mode. If this skill is used for a substantive final artifact, treat the default as deep investigation and manage scope by claim strength, evidence access, and explicit unresolved gaps.

## Stage 1A: Research Plan Card

Before broad search, create a lightweight research plan card. Do not stop for user input unless a missing choice would materially change the artifact or evidence boundary. Include:

```text
research question
target claim strength
requested final artifact genre
target audience
3-7 key leads or subquestions
priority source classes
required counter or support-limiting evidence
required execution, outcome, stakeholder, or freshness evidence when relevant
out-of-scope boundaries
downgrade rule if evidence is missing, stale, permission-gated, or contradicted
```

The plan card is an internal control surface, not the final artifact style. It should guide research behavior without forcing the final artifact into a fixed diagnostic format.

## Stage 2: Evidence Source Policy

Load `evidence-source-policy.md`. Classify sources before treating material as evidence.

Also load `sourceguard-discovery-loop.md` for substantive investigations. Use it to decide where evidence should be searched next, which source roles are missing, what access gaps exist, and when a claim must be downgraded because source discovery is incomplete.

## Stage 3: Logic-Lead Map

Before broad writing, create a lightweight lead map. Each important lead should have:

```text
lead question or hypothesis
why it matters to the user's requested conclusion
known support
counter or support-limiting evidence
unresolved gaps
current status: confirmed | supported-incomplete | candidate | contradicted | access-gap | not-supported
report eligibility: finding | qualified finding | hypothesis | omit | follow-up
```

Typical lead classes:

- event fact: what happened, when, where, and with whom;
- actor motive: why each actor may have acted;
- historical mechanism: what prior pattern explains the event;
- outcome claim: what was allegedly achieved;
- execution evidence: what has actually happened after the claim;
- contradiction or limitation: what weakens or narrows a claim;
- future impact: what later evidence would confirm or falsify the projection.

Depth is judged by lead coverage and evidence-chain status, not by the number of sources collected.

## Stage 3A: General Evidence-Role Map

For every substantive investigation, split the apparent story into evidence roles before writing:

```text
claim origin or rumor source
direct/original fact record
source statement or actor claim
scope and boundary evidence
execution, outcome, or impact evidence
context, motive, or constraint evidence
expert, media, or analyst interpretation
counter, limiting, or non-occurrence evidence
future hypothesis and observable trigger conditions
```

Each role needs a status, source markers, and claim-use label. Context, motive, expert commentary, or market concern can explain why a claim is plausible, but they do not prove execution, outcome, causality, or broader scope unless a bridging source establishes that link.

For a negative or partial finding, record which evidence roles or concrete signals were searched, absent, access-gated, or not applicable. Search failure alone is not proof of absence unless the searched source set is strong enough for that claim.

## Stage 4: SourceGuard Discovery Plan

Before broad search, build or update a SourceGuard discovery state:

```text
case goal
claim strength target
lead map
required evidence roles
known source candidates
public/local/internal permissions
access gaps
contradictions or weak source coverage
next search actions with expected value
handoff targets for TraceGuard and LogicGuard
```

Use SourceGuard to rank the first search batch across public, local, internal, counter, limiting, and follow-up evidence directions. SourceGuard scores source-discovery value only; they do not prove a claim.

## Stage 5: First-Round Search

Search several directions when relevant:

- timeline;
- actors;
- location;
- cause;
- impact;
- contradiction;
- missing proof;
- follow-up consequences;
- public record;
- local or internal record when allowed.

Use the SourceGuard-ranked plan as the default order unless the user has a stricter deadline, permission boundary, or target artifact need. Save found items as source candidates first, not as conclusions.

## Stage 6: SourceGuard Observation Update

After each meaningful search batch, write observations back into the SourceGuard state:

```text
source found
source role covered
lead or claim affected
freshness and coverage-period clues
access result
contradiction or limitation discovered
new search lead
handoff readiness
```

If an important evidence role is still missing, route the gap back through SourceGuard before promoting the material to TraceGuard or LogicGuard. If the missing role cannot be searched under the current permissions, record an access gap and downgrade the claim boundary.

## Stage 6A: Per-Round Replan Gate

After each meaningful search or source-reading batch, choose and record one next move before drafting final claims:

```text
continue deepening the same lead
switch source class or search tactic
seek counter or limiting evidence
seek execution, outcome, stakeholder, or freshness evidence
route stable event material to TraceGuard
route stable source support to LogicGuard
downgrade the claim
stop and state the unresolved gap
```

Use the replan gate to prevent linear "search once, write confidently" behavior. If a new source changes the target artifact, audience, conclusion strength, or evidence policy, mark earlier validation evidence stale and update the plan card.

## Stage 7: TraceGuard Case Library

Create or reuse:

```text
case -> lead/direction -> source -> evidence -> event/explanation candidate -> trace/storyline -> gap/contradiction -> claim boundary
```

Use TraceGuard for messy case material, weak signals, and gaps. Keep rejected or weak directions visible when they may prevent repeated failed searches.

## Stage 8: TraceGuard Evaluation

Build and evaluate a TraceGuard model. Record:

- storyline candidates;
- lead map and lead status;
- validated, candidate, weak, or contradicted status;
- timeline;
- event-chain table;
- explanation-chain table;
- evidence-chain state for each important lead;
- gap ledger;
- contradiction ledger;
- safe and unsafe wording guidance;
- suggested next evidence.

## Stage 9: Gap-Driven Search Loop

Route important gaps:

```text
missing public evidence -> SourceGuard public search action
missing local evidence -> SourceGuard local file / Drive / notes / logs action if allowed
missing internal evidence -> SourceGuard internal source action if allowed
missing source permission -> access gap
missing warrant or explanation -> LogicGuard model gap
conflicting evidence -> TraceGuard contradiction review
one-sided evidence -> SourceGuard counter/limiting source action
claimed outcome without execution evidence -> SourceGuard execution follow-up action
missing stakeholder view -> SourceGuard stakeholder action
future-impact claim -> SourceGuard observable-trigger action
```

Loop through SourceGuard plan, search, save, observe, TraceGuard extract/evaluate, LogicGuard warrant review, and gap write-back until the claim strength is supported or downgraded.

## Stage 9A: Minimum Investigation Rounds

For any final artifact that claims to be detailed, complete, comprehensive, conclusive, or deep, run these rounds before final prose:

```text
official/original fact round: what happened, according to primary or closest available records
counter/limiting round: what weakens, narrows, contradicts, or fails to support the claim
impact/execution round: what actual effects, implementation, outcomes, or market/process changes can be observed
stakeholder round: what affected actors, institutions, experts, users, residents, companies, or opponents say or do
future-trigger round: what later evidence would confirm, falsify, or materially change the current conclusion
```

Do not treat these as source-count quotas. A round is complete only when its lead status is recorded as supported, contradicted, access-gap, not-supported, or deliberately downgraded. If an important round is incomplete, label the output as an initial investigation, staged artifact, qualified finding, or downgraded conclusion.

## Stage 10: Explicit LogicGuard Promotion

Promote only selected sources that are stable, important to the final claim, and worth formal preservation. Do not bulk-copy the TraceGuard case into LogicGuard.

SourceGuard candidates may point to material worth preserving, but promotion requires source stability, claim importance, and clear relevance to the final reasoning path.

## Stage 11: LogicGuard Modeling And Deepening

Model root claims, support, warrants, assumptions, rebuttals, limitations, and scope. Deepen high-importance or weak nodes before writing confident prose.

## Stage 12: Claim-To-Source Matrix

Before final prose, create a matrix that links important claims to source roles:

```text
claim or target artifact locator
lead id
source ids
source role: event fact | official claim | independent report | limiting evidence | expert analysis | historical background | hypothesis
source date or freshness
claim use: direct support | scope limiter | contrast | context | forecast trigger
claim strength
required inline citation marker
missing support or limitation
final prose treatment: main text | footnote | appendix | omitted with reason
```

Every important factual claim, official-claim report, analytic inference, limitation, and future hypothesis needs a citation marker or an explicit reason it is uncited background.

## Stage 13: Artifact Synthesis

Create a target story plan before final prose. The requested artifact genre controls final organization and tone. Common profiles:

```text
news-style article
research report
internal briefing
incident review
policy memo
paper-style long report
executive summary
literature review
decision note
deck storyline
```

The story plan should include section order, section handoffs, paragraph or artifact-location blueprints for core sections, and where inline citations must appear. Coverage obligations may be satisfied through narrative prose, compact citations, footnotes, tables, or appendix. Do not force evidence-role categories into visible headings unless that improves the requested artifact.

For long artifacts, add a reader route at the start of the plan:

```text
first question answered
why section 2 follows section 1
where contradictory or limiting evidence appears
where future-impact material begins
what is appendix-only
```

## Stage 14: Citation-Grounded Drafting

Write final prose from the story plan and claim-to-source matrix. Each core paragraph should make clear:

- what it claims;
- which lead it resolves;
- which source markers support or limit it;
- whether it is fact, official claim, analysis, or hypothesis.

## Stage 15: Final Claim Audit

Audit final prose for overclaiming, missing warrant, hidden assumption, unsupported causality, scope mismatch, unanswered rebuttal, missing limitation, and candidate claims written as confirmed.

Also audit for missing inline citations, source-role confusion, unsupported synthesis, missing counter/limiting evidence, official or actor claims written as independent facts, inferences written as facts, and section transitions that leave the reasoning path unclear.

If the audit fails because source coverage is missing, return to SourceGuard for a targeted search action. If it fails because event interpretation or contradiction handling is weak, return to TraceGuard. If it fails because the warrant or argument boundary is weak, return to LogicGuard. If the missing material cannot be obtained, weaken the claim or move it to hypothesis/unresolved.

## Stage 15A: Reader-Facing Artifact Cleanup

Before final delivery, clean the reader-facing final artifact:

- remove internal Guard-family terms such as `SourceGuard`, `TraceGuard`, `LogicGuard`, `FlowGuard`, and `History Ledger` unless the user explicitly asked for a methods appendix;
- replace them with ordinary language such as source search plan, event chain, evidence chain, argument structure, process check, source appendix, or run notes;
- keep method details, command evidence, and run bookkeeping in the appendix or local ledger;
- verify each core paragraph says who is speaking or what type of source supports the point when that matters;
- verify the section, paragraph, page, slide, or artifact order follows the reader route rather than a tool log.

## Stage 16: FlowGuard Closure

Use FlowGuard to check stage order, artifact versions, validations, stale evidence, revalidation, and completion boundaries.

## Stage 17: Final Delivery

Load `output-contract.md`. Deliver readable prose first, appendix second.

## Stage 18: History Postflight

Write the run record, artifact pointers, reusable search directions, failed routes, unresolved gaps, privacy labels, and closure status.
