# FlowGuard Closure

Use FlowGuard to guard process order, evidence freshness, revalidation, local-output privacy, and honest completion claims for this orchestration skill.

## Boundary

FlowGuard answers:

```text
Was the investigation process current, ordered, and honestly closed?
```

It does not reconstruct storylines, audit factual truth, or replace TraceGuard or LogicGuard.

Do not modify the standalone FlowGuard skill to enforce research artifact content rules. The research-specific checks below are this skill's closure contract for how it uses FlowGuard.

SourceGuard belongs before TraceGuard and LogicGuard in the default heavy-investigation process. FlowGuard closure should treat a missing SourceGuard discovery pass as a skipped process step unless the investigation is trivial, already has all required sources, or the user explicitly scoped the work to existing material only.

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
- research plan card, including target claim strength, requested final artifact genre, required counter/limiting evidence, and downgrade rule;
- SourceGuard source-discovery state, planned search actions, observations, candidate sources, source-role coverage, and access gaps;
- per-round replanning decisions after meaningful search or source-reading batches;
- logic-lead map and current lead statuses;
- general evidence-role map: claim origin, direct facts, source claims, scope, execution/outcome, context/motive, interpretation, counter/limiting evidence, and future triggers;
- minimum investigation round status: original-fact, counter/limiting, impact/execution, stakeholder, and future-trigger rounds;
- checked concrete signals and missing-signal list when execution, outcome, causality, broader scope, or negative findings are material;
- History Ledger preflight result;
- TraceGuard case material and model;
- TraceGuard evaluations, gaps, contradictions, and reports;
- TraceGuard event/explanation/evidence-chain handoff;
- LogicGuard promoted sources and argument models;
- LogicGuard claim-to-source matrix;
- LogicGuard section/paragraph/artifact-location blueprint;
- reader route and section, page, slide, or artifact handoffs for long artifacts;
- LogicGuard synthesis plan and final audit;
- reader-facing final artifact cleanup and internal-term leak check;
- final artifact and appendix or support material;
- History Ledger postflight record.

## Freshness Rules

Treat earlier evidence as stale when:

- SourceGuard search actions or observations change after TraceGuard evaluation;
- new evidence is added after TraceGuard evaluation;
- a contradiction is found after a storyline was accepted;
- promoted sources change after LogicGuard modeling;
- final prose changes after LogicGuard claim audit;
- citation markers, claim-to-source matrix, or section blueprint change after LogicGuard audit;
- user goal, target audience, conclusion strength, requested artifact genre, or evidence policy changes;
- local/internal access changes after an access gap was recorded.

Do not claim completion from stale, skipped, failed, or progress-only evidence.

## Minimum Closure Review

Before final delivery, check:

1. Did history preflight run?
2. Was the evidence-source policy explicit?
3. Did the research plan card record the target claim strength, final artifact genre, required counter/limiting evidence, and downgrade rule?
4. Did SourceGuard plan or reuse source-discovery actions for important leads and evidence roles?
5. Were SourceGuard observations written back after search batches, including failed searches and access gaps?
6. Did each meaningful source batch have a replanning decision before final claims were drafted?
7. Were sources saved before conclusions?
8. Did TraceGuard evaluate important storylines and gaps?
9. Were important logic leads mapped, pursued, downgraded, accepted as gaps, or marked blocked?
10. Were important gaps either searched through SourceGuard, downgraded, accepted, or marked blocked?
11. Were stable sources promoted to LogicGuard explicitly?
12. Does the final artifact have inline citation markers or artifact-appropriate source markers for important claims?
13. Did the underlying reasoning separate claim origin, direct facts, source statements, scope limits, execution/outcome evidence, context/motive, interpretation, counter/limiting evidence, and future triggers?
14. Did the official/original fact, counter/limiting, impact/execution, stakeholder, and future-trigger rounds complete, or was the output downgraded?
15. For negative or partial findings, were missing evidence roles or concrete signals named instead of silently assumed?
16. Did long artifacts include a reader route, handoffs, and paragraph/page/slide jobs before final prose?
17. Did LogicGuard audit final claims after final prose changes?
18. Did the reader-facing final artifact avoid internal Guard-family terms unless the user asked for a methods appendix?
19. Did new SourceGuard observations, new evidence, or artifact edits stale earlier checks?
20. Are generated final artifacts, case libraries, source libraries, and ledgers local-only or ignored unless explicitly approved for publication?
21. If a skill source was changed, was the installed skill copy synced and parity checked?
22. Was the History Ledger postflight written or explicitly blocked?

## Closure Status

Use one of:

- `passed`: all required stages and current checks completed.
- `partial`: useful output delivered, but accepted gaps or budget limits remain.
- `blocked`: critical access, evidence, tooling, or user decision prevents the requested conclusion strength.
- `downgraded`: final claim strength was lowered to match available evidence.

State closure status in the final appendix and History Ledger.

## Local Output And Git Boundary

By default, investigation outputs are runtime data, not software source:

- final artifacts and appendices;
- TraceGuard cases and models;
- LogicGuard source libraries and models;
- History Ledger run records;
- raw source snapshots.

Keep them local and ignored when the work happens inside a skill/software repository. Commit only skill code, public references, validation scripts, OpenSpec artifacts, and other software-source material unless the user explicitly requests a sanitized sample fixture.
