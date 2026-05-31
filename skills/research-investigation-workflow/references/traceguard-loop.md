# TraceGuard Loop

Use TraceGuard for messy investigation material, evidence-to-event reconstruction, storyline candidates, gaps, contradictions, and claim boundaries.

## Boundary

TraceGuard answers:

```text
What story does the evidence support?
```

It does not write final truth claims. It does not replace LogicGuard final claim audit.

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
source -> evidence -> event -> trace/storyline -> gap ledger -> contradiction ledger -> claim boundary
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

## Gap-Driven Loop

For each important gap, decide:

- Is a public search likely to help?
- Is a local or internal search allowed and likely to help?
- Is this an access gap?
- Is this a warrant or explanation gap for LogicGuard?
- Is this a contradiction that needs TraceGuard review?
- Should the claim be downgraded instead of searched further?

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

Pass only stable, important, selected support to LogicGuard. Do not bulk-promote the whole case.
