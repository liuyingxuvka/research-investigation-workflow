# FlowGuard Closure

Use FlowGuard to guard process order, evidence freshness, revalidation, and honest completion claims.

## Boundary

FlowGuard answers:

```text
Was the investigation process current, ordered, and honestly closed?
```

It does not reconstruct storylines, audit factual truth, or replace TraceGuard or LogicGuard.

## Current Command Surface Check

Before relying on a concrete command, check:

```powershell
python -c "import flowguard; print(flowguard.SCHEMA_VERSION)"
python -c "import importlib.metadata as m; print(m.version('flowguard'))"
python -m flowguard --help
```

For a project with FlowGuard adoption:

```powershell
python -m flowguard project-audit --root .
python .flowguard\development_process_flow\run_checks.py
```

## What To Track

Track these artifacts and versions:

- user goal and evidence-source policy;
- History Ledger preflight result;
- TraceGuard case material and model;
- TraceGuard evaluations, gaps, contradictions, and reports;
- LogicGuard promoted sources and argument models;
- LogicGuard synthesis plan and final audit;
- final report and appendix;
- History Ledger postflight record.

## Freshness Rules

Treat earlier evidence as stale when:

- new evidence is added after TraceGuard evaluation;
- a contradiction is found after a storyline was accepted;
- promoted sources change after LogicGuard modeling;
- final prose changes after LogicGuard claim audit;
- user goal, target audience, conclusion strength, or evidence policy changes;
- local/internal access changes after an access gap was recorded.

Do not claim completion from stale, skipped, failed, or progress-only evidence.

## Minimum Closure Review

Before final delivery, check:

1. Did history preflight run?
2. Was the evidence-source policy explicit?
3. Were sources saved before conclusions?
4. Did TraceGuard evaluate important storylines and gaps?
5. Were important gaps either searched, downgraded, accepted, or marked blocked?
6. Were stable sources promoted to LogicGuard explicitly?
7. Did LogicGuard audit final claims after final prose changes?
8. Did new evidence stale earlier checks?
9. Was the History Ledger postflight written or explicitly blocked?

## Closure Status

Use one of:

- `passed`: all required stages and current checks completed.
- `partial`: useful output delivered, but accepted gaps or budget limits remain.
- `blocked`: critical access, evidence, tooling, or user decision prevents the requested conclusion strength.
- `downgraded`: final claim strength was lowered to match available evidence.

State closure status in the final appendix and History Ledger.
