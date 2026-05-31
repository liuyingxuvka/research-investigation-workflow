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
- report type;
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

If the user has not specified a conclusion strength, default to `working hypothesis` for a quick pass and `evidence-backed finding` for a report request.

Do not ask the user to choose a shallow/medium/deep mode. If this skill is used for a substantive report, treat the default as deep investigation and manage scope by claim strength, evidence access, and explicit unresolved gaps.

## Stage 2: Evidence Source Policy

Load `evidence-source-policy.md`. Classify sources before treating material as evidence.

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

## Stage 3A: Policy-Rumor And Current-Event Ladder

When the user asks about a possible new policy, regulatory event, market rumor, or "new clue", split the apparent event into evidence roles before writing:

```text
trigger claim or rumor
official action actually found
jurisdiction and population in scope
implementation evidence: rule, tax rate, effective date, agency guidance, city list, budget treatment, enforcement data
market or execution data
fiscal, political, or actor-motive context
expert or media interpretation
future hypothesis and observable triggers
```

Each role needs a status and source markers. Fiscal pressure, actor motive, expert commentary, or market fear can explain why a policy is plausible, but they are not implementation evidence. A local pilot action is not national rollout evidence unless a national source creates that link.

For a negative or partial finding, record which implementation signals were searched, absent, access-gated, or not applicable. Search failure alone is not proof of absence unless the searched source set is strong enough for that claim.

## Stage 4: First-Round Search

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

Save found items as sources first, not as conclusions.

## Stage 5: TraceGuard Case Library

Create or reuse:

```text
case -> lead/direction -> source -> evidence -> event/explanation candidate -> trace/storyline -> gap/contradiction -> claim boundary
```

Use TraceGuard for messy case material, weak signals, and gaps. Keep rejected or weak directions visible when they may prevent repeated failed searches.

## Stage 6: TraceGuard Evaluation

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

## Stage 7: Gap-Driven Search Loop

Route important gaps:

```text
missing public evidence -> public search
missing local evidence -> local file / Drive / notes / logs search if allowed
missing internal evidence -> internal source search if allowed
missing source permission -> access gap
missing warrant or explanation -> LogicGuard model gap
conflicting evidence -> TraceGuard contradiction review
one-sided evidence -> counter/limiting source search
claimed outcome without execution evidence -> execution follow-up search
```

Loop through search, save, extract, rebuild, evaluate, and write back gaps until the claim strength is supported or downgraded.

## Stage 8: Explicit LogicGuard Promotion

Promote only selected sources that are stable, important to the final claim, and worth formal preservation. Do not bulk-copy the TraceGuard case into LogicGuard.

## Stage 9: LogicGuard Modeling And Deepening

Model root claims, support, warrants, assumptions, rebuttals, limitations, and scope. Deepen high-importance or weak nodes before writing confident prose.

## Stage 10: Claim-To-Source Matrix

Before final prose, create a matrix that links important claims to source roles:

```text
claim or paragraph target
lead id
source ids
source role: event fact | official claim | independent report | limiting evidence | expert analysis | historical background | hypothesis
source date or freshness
claim use: direct support | scope limiter | contrast | context | forecast trigger
claim strength
required inline citation marker
missing support or limitation
```

Every important factual claim, official-claim report, analytic inference, limitation, and future hypothesis needs a citation marker or an explicit reason it is uncited background.

## Stage 11: Artifact Synthesis

Create a target story plan before final prose. Common profiles:

```text
news-style article
research report
internal briefing
incident review
policy memo
paper-style long report
executive summary
```

The story plan should include section order, section handoffs, paragraph blueprints for core sections, and where inline citations must appear.

For long reports, add a reader route at the start of the plan:

```text
first question answered
why section 2 follows section 1
where contradictory or limiting evidence appears
where future-impact material begins
what is appendix-only
```

## Stage 12: Citation-Grounded Drafting

Write final prose from the story plan and claim-to-source matrix. Each core paragraph should make clear:

- what it claims;
- which lead it resolves;
- which source markers support or limit it;
- whether it is fact, official claim, analysis, or hypothesis.

## Stage 13: Final Claim Audit

Audit final prose for overclaiming, missing warrant, hidden assumption, unsupported causality, scope mismatch, unanswered rebuttal, missing limitation, and candidate claims written as confirmed.

Also audit for missing inline citations, source-role confusion, unsupported synthesis, and section transitions that leave the reasoning path unclear.

If the audit fails, search more, weaken the claim, or move it to hypothesis/unresolved.

## Stage 14: FlowGuard Closure

Use FlowGuard to check stage order, artifact versions, validations, stale evidence, revalidation, and completion boundaries.

## Stage 15: Final Delivery

Load `output-contract.md`. Deliver readable prose first, appendix second.

## Stage 16: History Postflight

Write the run record, artifact pointers, reusable search directions, failed routes, unresolved gaps, privacy labels, and closure status.
