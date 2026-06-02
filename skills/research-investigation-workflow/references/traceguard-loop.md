# TraceGuard Loop

Use TraceGuard for messy investigation material, evidence-to-event reconstruction, logic leads, explanation candidates, competing storyline candidates, causal-chain status, counterfactual traces, confounder ledgers, gaps, contradictions, and claim boundaries. Use SourceGuard before TraceGuard when the task still needs source discovery planning, branch-aware source search, source-role coverage, counter-source search, or access-gap routing.

## Boundary

TraceGuard answers:

```text
What story does the evidence support?
```

It does not write final truth claims. It does not replace LogicGuard final claim audit. It should separate event facts from explanation leads: evidence that an event happened is not automatically evidence for motive, outcome, future impact, or superiority over alternative explanations.

For substantive investigations, TraceGuard should also separate claim origin, direct facts, source statements, scope boundaries, execution or outcome evidence, context or motive evidence, interpretation, counter or limiting evidence, and future triggers. Context can explain why a claim is plausible, but it does not validate execution, causality, outcome, or broader scope.

Keep three claim layers separate:

```text
event fact: what happened, when, where, and who is involved
explanation: why it happened, what mechanism or motive is supported
outcome or impact: what changed, operated, shipped, failed, improved, or harmed
```

Evidence for one layer does not validate the others. An official announcement may support a source statement; it does not establish execution or outcome without execution/outcome evidence. Motive or context evidence may support plausibility; it does not establish causality without a warrant and bridging evidence.

For substantive investigations, use a layered lead model rather than one coarse storyline:

```text
lead
event fact layer
explanation layer
execution or follow-through layer
outcome or impact layer
stakeholder or affected-party layer
counter, delay, contradiction, or non-occurrence layer
future trigger layer
safe wording and unsafe wording
```

The model can stay lightweight, but every high-impact lead should show which layer is supported and which layer remains candidate, weak, access-gap, or not-supported.

For follow-through claims, maintain an explicit execution chain:

```text
announcement or claim
planned action
implementation signal
operating or outcome signal
affected-stakeholder signal
counter, delay, cancellation, non-occurrence, or limiting signal
future trigger that would change the conclusion
```

If the chain stops at announcement or plan, the safe wording must say that execution or outcome evidence is missing.

For price, market, policy, adoption, causal, reliability, performance, or other effect claims, maintain an effect chain:

```text
driver or proposed cause
mechanism
intermediate signal
observed outcome or impact
affected-stakeholder signal
counter or limiting evidence
alternative drivers or confounders
future trigger
weakest link
safe wording
unsafe wording
```

Do not let an intermediate signal become the final effect. Planning pressure, capacity-market movement, wholesale price movement, transmission cost, retail bill impact, and stakeholder harm are separate effect layers unless bridge evidence links them.

For Atlas-driven work, preserve competing storylines instead of prematurely forcing one clean narrative:

```text
storyline id
storyline claim
supporting evidence
opposing evidence
alternative explanation relationship
confounders or scope limits
causal-chain state
counterfactual question
safe wording
unsafe wording
next evidence need
```

The strongest opposing storyline should be explicit when it materially affects the final conclusion.

SourceGuard answers a different question:

```text
Which source should be searched or preserved next?
```

Do not make TraceGuard carry candidate-source ranking or permission planning. Hand SourceGuard results into TraceGuard only after a source candidate has been found, preserved, and given an evidence role.

## Current Command Surface Check

Before relying on a specific command, check:

```powershell
python -m traceguard --help
python -m traceguard library --help
```

Use project-specific help output over stale remembered command syntax.

## Case Library Shape

Use or create:

```text
SourceGuard source action -> lead/direction -> source -> evidence -> event fact or explanation candidate -> trace/storyline -> gap ledger -> contradiction ledger -> claim boundary
```

For report-grade or paper-grade investigations, case evidence should preserve enough structure to rebuild:

```text
case -> lead -> source -> evidence anchor -> event fact -> explanation candidate -> execution/follow-through state -> effect-chain state -> competing storyline -> gap/contradiction -> safe wording
```

Suggested commands when available:

```powershell
python -m traceguard library init <library-root>
python -m traceguard library create-case <library-root> <case-id>
python -m traceguard library add-direction <library-root> <case-id> <direction-id>
python -m traceguard library add-source <library-root> <case-id> <direction-id>
python -m traceguard library add-evidence <library-root> <case-id> <direction-id>
python -m traceguard library build-model <library-root> <case-id> --output <model.yaml>
```

## Evaluation

Run the strongest practical checks for the current model:

```powershell
python -m traceguard validate <model.yaml>
python -m traceguard evaluate <model.yaml> --pretty
python -m traceguard diagnose <model.yaml> --pretty
python -m traceguard gaps <model.yaml> --pretty
python -m traceguard report <model.yaml> --format markdown
```

When final writing begins, export LogicGuard-ready support if the command is available:

```powershell
python -m traceguard export-logicguard <model.yaml> --output trace_logicguard_bundle.yaml
```

## Lead And Evidence-Chain Handoff

Before handing material to LogicGuard, produce or maintain a compact handoff:

```text
lead id
lead question or hypothesis
event facts involved
explanation hypothesis involved
follow-up impact or outcome claim
effect-chain layer and weakest link
supporting evidence ids
source registry ids
counter or support-limiting evidence ids
missing evidence
status: confirmed | supported-incomplete | candidate | weak | contradicted | access-gap | not-supported
safe wording
unsafe wording
next search direction
```

Recommended tables:

- event chain: date, event, source, evidence status, claim boundary;
- three-layer lead table: event fact, explanation hypothesis, follow-up impact or outcome;
- evidence-role table: claim origin, direct fact, source statement, scope, execution/outcome, context/motive, interpretation, counter/limiting evidence, future trigger;
- explanation chain: candidate explanation, supporting evidence, limiting evidence, current status;
- execution chain: announced outcome, implementation evidence, missing execution proof;
- effect or transmission chain: driver, mechanism, intermediate signal, outcome signal, stakeholder signal, counter evidence, weakest link, safe wording;
- non-occurrence or delay chain when the investigation checks whether an expected follow-up has not happened;
- contradiction/gap table: conflict or gap, affected lead, needed evidence, action.
- competing storyline table: storyline, support, opposition, gaps, safe wording, final treatment;
- causal chain table: proposed cause, mechanism, effect, evidence for each link, weakest link;
- counterfactual trace table: proposed cause, what might happen without it, evidence need, claim impact;
- confounder ledger: alternative driver, evidence status, affected branch, next action.

Do not pass a lead to final prose as a finding unless its status and safe wording support that strength.

Before handing material to LogicGuard, check:

```text
lead status known
event evidence anchored
explanation evidence separated from event evidence
outcome or impact evidence separated from announcement/context evidence
execution chain status recorded for follow-through claims
effect-chain status recorded for price, market, policy, causal, adoption, or impact claims
counter or limiting evidence considered
safe wording available
unsafe wording listed when overclaim risk is material
missing evidence identified
access gaps carried forward
```

If the handoff is incomplete, either route the missing evidence need back to SourceGuard, keep the lead as candidate/weak/access-gap, or downgrade the final artifact claim.

## Gap-Driven Loop

For each important gap, decide:

- Should this gap return to SourceGuard for a ranked public, local, internal, counter, limiting, stakeholder, or future-trigger search?
- Is a local or internal search allowed and likely to help, or should it be marked as an access gap?
- Is this an access gap?
- Is this a warrant or explanation gap for LogicGuard?
- Is this a contradiction that needs TraceGuard review?
- Should the claim be downgraded instead of searched further?
- Is there only positive/supporting evidence, requiring a counter or limiting-source search?
- Is this an outcome claim that requires later execution evidence?
- Is this a future-impact claim that needs observable trigger conditions?
- Does this claim require a concrete execution, outcome, causal, scope, or stakeholder signal that is still missing?
- Is the final prose likely to imply execution, outcome, causality, or scope that the trace only supports as announcement, context, or hypothesis?
- Is the final prose likely to imply national scope from local or regional evidence, observed fact from forecast/model evidence, retail impact from wholesale/capacity/planning evidence, or sector-wide impact from actor-specific evidence?
- Does a competing storyline remain viable enough to require LogicGuard conclusion tournament review?
- Does a counterfactual path show that the outcome may occur without the proposed main cause?

After new evidence:

1. Update SourceGuard observations for the search action.
2. Save the source.
3. Extract evidence.
4. Update events and trace.
5. Rebuild or update the model.
6. Rerun evaluation and diagnostics.
7. Write back gaps to TraceGuard and SourceGuard if the libraries support it.

When sources conflict, do not resolve the conflict by averaging or by selecting the smoothest story. Record:

- which source conflicts with which;
- which source is fresher;
- which source is closer to the event;
- which source has stronger locator or provenance;
- whether the conflict affects event fact, explanation, outcome, or scope;
- whether SourceGuard follow-up, LogicGuard warrant review, or claim downgrade is required.

When source scope or effect layer conflicts with desired final wording, record a scope-transfer warning:

```text
transfer type: local-to-national | actor-to-sector | forecast-to-fact | wholesale-to-retail | planning-to-outcome | announcement-to-operation | chronology-to-causality | interpretation-to-direct-fact
current evidence layer
desired wording layer
bridge evidence found or missing
safe wording
```

Suggested write-back:

```powershell
python -m traceguard library write-back-gaps <library-root> <case-id> --result <evaluation.json>
```

## Claim Boundary Output

Keep wording guidance explicit:

- `supported`: safe to state with cited support.
- `candidate`: present as provisional.
- `weak`: present only as a lead or omit.
- `contradicted`: do not state as finding unless scoped to the contradiction.
- `access_gap`: state that support could not be checked.
- `supported-incomplete`: state as a qualified finding and name the missing evidence.
- `not-supported`: omit as a claim or move to a rejected lead.

Pass only stable, important, selected support to LogicGuard. Do not bulk-promote the whole case.

Before final writing handoff, provide safe/unsafe wording for every high-impact lead where source roles could be confused. Typical unsafe wording includes treating an official statement as independent fact, treating announcement as execution, treating motive/context as causality, or treating no discovered source as proof of absence without a strong searched-source set.

For effect claims, unsafe wording also includes treating capacity, wholesale, planning, resource-procurement, pilot, queue, forecast, or company-announcement evidence as terminal outcome, retail, national, or stakeholder-impact evidence without bridge support.

For Atlas-driven handoff, also provide:

```text
competing storyline ids
causal-chain weakest links
counterfactual trace status
confounder ledger summary
red-team storyline
branches that need SourceGuard search
claims that need LogicGuard conclusion tournament
```
