## flowguard-project-adopt - FlowGuard project adopt record update

- Project: ResearchInvestigationWorkflow_20260531
- Trigger reason: target project uses FlowGuard and needs durable AGENTS/version records
- Status: completed
- Skill decision: used_flowguard
- Started: 2026-05-31T10:47:55+00:00
- Ended: 2026-05-31T10:47:55+00:00
- Duration seconds: 0.000
- Commands OK: True

### Model Files
- none recorded

### Commands
- none recorded

### Findings
- FlowGuard repository recorded: https://github.com/liuyingxuvka/FlowGuard
- FlowGuard package version recorded: 0.39.1
- FlowGuard schema version recorded: 1.0

### Counterexamples
- none recorded

### Friction Points
- none recorded

### Skipped Steps
- Project adoption record does not replace executable model checks, tests, replay, or closure evidence.

### Risk Evidence Summary
- none recorded

### Next Actions
- Rerun affected FlowGuard models/tests before broad completion claims when behavior, tests, or version records change.


## research-investigation-workflow-skill-20260531 - Create research-investigation-workflow Codex skill

- Project: ResearchInvestigationWorkflow_20260531
- Trigger reason: Non-trivial skill/process implementation with OpenSpec artifacts, installed skill sync, validation evidence freshness, and closure claim
- Status: in_progress
- Skill decision: use_direct_flowguard_skill: existing_model_preflight plus development_process_flow
- Started: 2026-05-31T10:49:16+00:00
- Ended: 2026-05-31T10:49:16+00:00
- Duration seconds: 0.000
- Commands OK: True

### Model Files
- .flowguard\existing_model_preflight\model.py
- .flowguard\development_process_flow\model.py

### Commands
- OK (0.000s): `python -c import flowguard; print(flowguard.SCHEMA_VERSION)`
- OK (0.000s): `python -m flowguard project-adopt --root . --json`

### Findings
- none recorded

### Counterexamples
- none recorded

### Friction Points
- none recorded

### Skipped Steps
- none recorded

### Risk Evidence Summary
- none recorded

### Next Actions
- none recorded


## research-investigation-workflow-skill-20260531 - Create research-investigation-workflow Codex skill

- Project: ResearchInvestigationWorkflow_20260531
- Trigger reason: Non-trivial skill/process implementation with OpenSpec artifacts, installed skill sync, validation evidence freshness, and closure claim
- Status: completed
- Skill decision: use_direct_flowguard_skill: existing_model_preflight plus development_process_flow
- Started: 2026-05-31T10:58:14+00:00
- Ended: 2026-05-31T10:58:14+00:00
- Duration seconds: 0.000
- Commands OK: True

### Model Files
- .flowguard\existing_model_preflight\model.py
- .flowguard\development_process_flow\model.py

### Commands
- OK (0.000s): `python .flowguard\existing_model_preflight\run_checks.py`
- OK (0.000s): `python .flowguard\development_process_flow\run_checks.py`
- OK (0.000s): `quick_validate.py installed and project skill copies`
- OK (0.000s): `openspec validate add-research-investigation-workflow-skill --strict`
- OK (0.000s): `installed/project skill hashes match`

### Findings
- Implemented thin orchestration skill without merging TraceGuard Case Library and LogicGuard Source Library
- OpenSpec tasks complete 21/21
- Git sync unavailable because workspace and installed skill path are not Git repositories

### Counterexamples
- none recorded

### Friction Points
- none recorded

### Skipped Steps
- none recorded

### Risk Evidence Summary
- FlowGuard broken routes intentionally block combined reasoning engine and stale validation after skill edits

### Next Actions
- Archive OpenSpec change if desired


## upgrade-investigation-depth-contract-20260531 - Upgrade research investigation depth, citation, and closure contract

- Project: ResearchInvestigationWorkflow_20260531
- Trigger reason: User corrected the depth model and FlowGuard ownership boundary for the research-investigation-workflow skill
- Status: completed
- Skill decision: use_direct_flowguard_skill: existing_model_preflight plus development_process_flow
- Started: 2026-05-31T13:33:00+00:00
- Ended: 2026-05-31T13:45:28+00:00
- Duration seconds: 0.000
- Commands OK: True

### Model Files
- .flowguard\existing_model_preflight\model.py
- .flowguard\development_process_flow\model.py

### Commands
- OK (0.000s): `python -c import flowguard, importlib.metadata as m; print(flowguard.SCHEMA_VERSION); print(m.version('flowguard'))`
- OK (0.000s): `python -m flowguard project-audit --root .`
- OK (0.000s): `python .flowguard\existing_model_preflight\run_checks.py`
- OK (0.000s): `python .flowguard\development_process_flow\run_checks.py`
- OK (0.000s): `openspec validate upgrade-investigation-depth-contract --strict`
- OK (0.000s): `quick_validate.py updated installed and local skill surfaces`
- OK (0.000s): `targeted rg text checks`
- OK (0.000s): `git check-ignore -v investigations .traceguard-cases .logicguard-library .research-investigation-history`

### Findings
- Deep investigation is now defined by logic leads and evidence chains rather than source counts or shallow/medium/deep modes.
- TraceGuard handoff now records lead questions, event facts, supporting evidence, limiting/counter evidence, missing evidence, and safe wording.
- LogicGuard report-writing routes now require claim-to-source matrices, paragraph or section blueprints, inline citation markers, and source-role labels.
- FlowGuard standalone skill was not changed; research-specific FlowGuard closure rules are encoded in research-investigation-workflow.
- Generated investigation outputs remain local-only and ignored by the software repository.

### Counterexamples
- none recorded

### Friction Points
- `quick_validate.py` requires the skill directory argument; running it from inside the skill directory without the argument returns usage text.

### Skipped Steps
- none recorded

### Risk Evidence Summary
- FlowGuard bad-route fixtures still block duplicate reasoning-engine ownership and stale validation evidence.
- No FlowGuard report-writing rule was added to the standalone FlowGuard skill.

### Next Actions
- Commit software-only changes in the three affected repositories.
- Record predictive KB postflight lesson.


## flowguard-project-upgrade - FlowGuard project upgrade record update

- Project: ResearchInvestigationWorkflow_20260531
- Trigger reason: target project uses FlowGuard and needs durable AGENTS/version records
- Status: completed
- Skill decision: used_flowguard
- Started: 2026-05-31T15:28:27+00:00
- Ended: 2026-05-31T15:28:27+00:00
- Duration seconds: 0.000
- Commands OK: True

### Model Files
- none recorded

### Commands
- none recorded

### Findings
- FlowGuard repository recorded: https://github.com/liuyingxuvka/FlowGuard
- FlowGuard package version recorded: 0.39.2
- FlowGuard schema version recorded: 1.0

### Counterexamples
- none recorded

### Friction Points
- none recorded

### Skipped Steps
- Project adoption record does not replace executable model checks, tests, replay, or closure evidence.

### Risk Evidence Summary
- none recorded

### Next Actions
- Rerun affected FlowGuard models/tests before broad completion claims when behavior, tests, or version records change.


## flowguard-project-upgrade - FlowGuard project upgrade record update

- Project: ResearchInvestigationWorkflow_20260531
- Trigger reason: target project uses FlowGuard and needs durable AGENTS/version records
- Status: completed
- Skill decision: used_flowguard
- Started: 2026-05-31T15:40:27+00:00
- Ended: 2026-05-31T15:40:27+00:00
- Duration seconds: 0.000
- Commands OK: True

### Model Files
- none recorded

### Commands
- none recorded

### Findings
- FlowGuard repository recorded: https://github.com/liuyingxuvka/FlowGuard
- FlowGuard package version recorded: 0.39.3
- FlowGuard schema version recorded: 1.0

### Counterexamples
- none recorded

### Friction Points
- none recorded

### Skipped Steps
- Project adoption record does not replace executable model checks, tests, replay, or closure evidence.

### Risk Evidence Summary
- none recorded

### Next Actions
- Rerun affected FlowGuard models/tests before broad completion claims when behavior, tests, or version records change.
