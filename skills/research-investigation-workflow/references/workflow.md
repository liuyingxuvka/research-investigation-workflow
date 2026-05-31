# End-To-End Workflow

Use this file for the default investigation route. Keep the work staged, and show when evidence, claims, or validation are partial.

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

Conclusion strength levels:

```text
initial leads
working hypothesis
evidence-backed finding
deep research conclusion
formal report / paper-grade conclusion
```

If the user has not specified a conclusion strength, default to `working hypothesis` for a quick pass and `evidence-backed finding` for a report request.

## Stage 2: Evidence Source Policy

Load `evidence-source-policy.md`. Classify sources before treating material as evidence.

## Stage 3: First-Round Search

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

## Stage 4: TraceGuard Case Library

Create or reuse:

```text
case -> direction -> source -> evidence -> event -> trace
```

Use TraceGuard for messy case material, weak signals, and gaps. Keep rejected or weak directions visible when they may prevent repeated failed searches.

## Stage 5: TraceGuard Evaluation

Build and evaluate a TraceGuard model. Record:

- storyline candidates;
- validated, candidate, weak, or contradicted status;
- timeline;
- gap ledger;
- contradiction ledger;
- safe and unsafe wording guidance;
- suggested next evidence.

## Stage 6: Gap-Driven Search Loop

Route important gaps:

```text
missing public evidence -> public search
missing local evidence -> local file / Drive / notes / logs search if allowed
missing internal evidence -> internal source search if allowed
missing source permission -> access gap
missing warrant or explanation -> LogicGuard model gap
conflicting evidence -> TraceGuard contradiction review
```

Loop through search, save, extract, rebuild, evaluate, and write back gaps until the claim strength is supported or downgraded.

## Stage 7: Explicit LogicGuard Promotion

Promote only selected sources that are stable, important to the final claim, and worth formal preservation. Do not bulk-copy the TraceGuard case into LogicGuard.

## Stage 8: LogicGuard Modeling And Deepening

Model root claims, support, warrants, assumptions, rebuttals, limitations, and scope. Deepen high-importance or weak nodes before writing confident prose.

## Stage 9: Artifact Synthesis

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

## Stage 10: Final Claim Audit

Audit final prose for overclaiming, missing warrant, hidden assumption, unsupported causality, scope mismatch, unanswered rebuttal, missing limitation, and candidate claims written as confirmed.

If the audit fails, search more, weaken the claim, or move it to hypothesis/unresolved.

## Stage 11: FlowGuard Closure

Use FlowGuard to check stage order, artifact versions, validations, stale evidence, revalidation, and completion boundaries.

## Stage 12: Final Delivery

Load `output-contract.md`. Deliver readable prose first, appendix second.

## Stage 13: History Postflight

Write the run record, artifact pointers, reusable search directions, failed routes, unresolved gaps, privacy labels, and closure status.
