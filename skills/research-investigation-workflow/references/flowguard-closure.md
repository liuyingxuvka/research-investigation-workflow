# FlowGuard Closure

Use FlowGuard to guard process order, evidence freshness, revalidation, local-output privacy, and honest completion claims for this orchestration skill.

## Boundary

FlowGuard answers:

```text
Was the investigation process current, ordered, and honestly closed?
```

It does not reconstruct storylines, audit factual truth, or replace TraceGuard or LogicGuard.

Do not modify the standalone FlowGuard skill to enforce research-report content rules. The research-specific checks below are this skill's closure contract for how it uses FlowGuard.

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
- logic-lead map and current lead statuses;
- policy-rumor/current-event role ladder when applicable;
- checked implementation signals and missing-signal list when a rollout, implementation, or negative finding is material;
- History Ledger preflight result;
- TraceGuard case material and model;
- TraceGuard evaluations, gaps, contradictions, and reports;
- TraceGuard event/explanation/evidence-chain handoff;
- LogicGuard promoted sources and argument models;
- LogicGuard claim-to-source matrix;
- LogicGuard section/paragraph blueprint;
- reader route and section handoffs for long reports;
- LogicGuard synthesis plan and final audit;
- final report and appendix;
- History Ledger postflight record.

## Freshness Rules

Treat earlier evidence as stale when:

- new evidence is added after TraceGuard evaluation;
- a contradiction is found after a storyline was accepted;
- promoted sources change after LogicGuard modeling;
- final prose changes after LogicGuard claim audit;
- citation markers, claim-to-source matrix, or section blueprint change after LogicGuard audit;
- user goal, target audience, conclusion strength, or evidence policy changes;
- local/internal access changes after an access gap was recorded.

Do not claim completion from stale, skipped, failed, or progress-only evidence.

## Minimum Closure Review

Before final delivery, check:

1. Did history preflight run?
2. Was the evidence-source policy explicit?
3. Were sources saved before conclusions?
4. Did TraceGuard evaluate important storylines and gaps?
5. Were important logic leads mapped, pursued, downgraded, accepted as gaps, or marked blocked?
6. Were important gaps either searched, downgraded, accepted, or marked blocked?
7. Were stable sources promoted to LogicGuard explicitly?
8. Does the final report have inline citation markers for important claims?
9. For policy or current-event rumors, did the report separate official action, jurisdiction/scope, implementation evidence, context/motive, expert commentary, and forecast?
10. For negative or partial findings, were missing implementation signals named instead of silently assumed?
11. Did long reports include a reader route, section handoffs, and paragraph jobs before final prose?
12. Did LogicGuard audit final claims after final prose changes?
13. Did new evidence or report edits stale earlier checks?
14. Are generated reports, case libraries, source libraries, and ledgers local-only or ignored unless explicitly approved for publication?
15. If a skill source was changed, was the installed skill copy synced and parity checked?
16. Was the History Ledger postflight written or explicitly blocked?

## Closure Status

Use one of:

- `passed`: all required stages and current checks completed.
- `partial`: useful output delivered, but accepted gaps or budget limits remain.
- `blocked`: critical access, evidence, tooling, or user decision prevents the requested conclusion strength.
- `downgraded`: final claim strength was lowered to match available evidence.

State closure status in the final appendix and History Ledger.

## Local Output And Git Boundary

By default, investigation outputs are runtime data, not software source:

- reports and appendices;
- TraceGuard cases and models;
- LogicGuard source libraries and models;
- History Ledger run records;
- raw source snapshots.

Keep them local and ignored when the work happens inside a skill/software repository. Commit only skill code, public references, validation scripts, OpenSpec artifacts, and other software-source material unless the user explicitly requests a sanitized sample fixture.
