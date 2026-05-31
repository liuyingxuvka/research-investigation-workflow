# TraceGuard Loop

Use TraceGuard for messy investigation material, evidence-to-event reconstruction, logic leads, explanation candidates, storyline candidates, gaps, contradictions, and claim boundaries.

## Boundary

TraceGuard answers:

```text
What story does the evidence support?
```

It does not write final truth claims. It does not replace LogicGuard final claim audit. It should separate event facts from explanation leads: evidence that an event happened is not automatically evidence for motive, outcome, or future impact.

For policy rumors or current-event "new clue" work, TraceGuard should also separate official action, jurisdiction/scope, implementation evidence, market or execution data, fiscal/motive context, expert commentary, and future hypothesis. Context can explain why a policy is plausible, but it does not validate rollout or execution.

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
lead/direction -> source -> evidence -> event fact or explanation candidate -> trace/storyline -> gap ledger -> contradiction ledger -> claim boundary
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
supporting evidence ids
counter or support-limiting evidence ids
missing evidence
status: confirmed | supported-incomplete | candidate | weak | contradicted | access-gap | not-supported
safe wording
unsafe wording
next search direction
```

Recommended tables:

- event chain: date, event, source, evidence status, claim boundary;
- policy/action ladder when applicable: trigger claim, official action, jurisdiction/scope, implementation signal, fiscal/context evidence, expert commentary, future trigger;
- explanation chain: candidate explanation, supporting evidence, limiting evidence, current status;
- execution chain: announced outcome, implementation evidence, missing execution proof;
- contradiction/gap table: conflict or gap, affected lead, needed evidence, action.

Do not pass a lead to final prose as a finding unless its status and safe wording support that strength.

## Gap-Driven Loop

For each important gap, decide:

- Is a public search likely to help?
- Is a local or internal search allowed and likely to help?
- Is this an access gap?
- Is this a warrant or explanation gap for LogicGuard?
- Is this a contradiction that needs TraceGuard review?
- Should the claim be downgraded instead of searched further?
- Is there only positive/supporting evidence, requiring a counter or limiting-source search?
- Is this an outcome claim that requires later execution evidence?
- Is this a future-impact claim that needs observable trigger conditions?
- Is this a policy implementation claim that requires implementing rule, covered jurisdiction, effective date, rate/standard, enforcement guidance, budget treatment, or execution data?

After new evidence:

1. Save the source.
2. Extract evidence.
3. Update events and trace.
4. Rebuild or update the model.
5. Rerun evaluation and diagnostics.
6. Write back gaps if the Case Library supports it.

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
