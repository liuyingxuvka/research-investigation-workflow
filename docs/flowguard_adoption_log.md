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


## add-research-reasoning-atlas-20260602 - Generic Research Reasoning Atlas upgrade

- Project: ResearchInvestigationWorkflow_20260531
- Trigger reason: User requested a general, non-domain-specific research upgrade aimed at deeper logic branching, pro/con alternatives, model lenses, expert stances, counterfactuals, and conclusion adjudication.
- Status: completed
- Skill decision: use_direct_flowguard_skill: existing_model_preflight plus development_process_flow; companion OpenSpec change add-research-reasoning-atlas
- Started: 2026-06-02T07:15:00+00:00
- Ended: 2026-06-02T07:52:13+00:00
- Commands OK: True

### Model Files
- .flowguard/existing_model_preflight/model.py
- .flowguard/development_process_flow/model.py

### Commands
- OK: `openspec validate add-research-reasoning-atlas --strict` -> change valid.
- OK: `openspec status --change add-research-reasoning-atlas` -> proposal, design, specs, and tasks complete.
- OK: `python .flowguard\existing_model_preflight\run_checks.py` -> valid route passed; duplicate-boundary fixture blocked as expected.
- OK: `python .flowguard\development_process_flow\run_checks.py` -> valid lifecycle passed; stale-validation fixture blocked as expected.
- OK: `python -m flowguard project-audit --root .` in ResearchWorkflow, SourceGuard, TraceGuard, and LogicGuard.
- OK: `quick_validate.py` for all upgraded installed skills.
- OK: Guard command-surface checks for SourceGuard, TraceGuard, TraceGuard Library, LogicGuard citation, synthesis, and structure commands.
- OK: Focused Guard example regressions for SourceGuard validate/plan, TraceGuard validate/diagnose, and LogicGuard validate/citation audit.
- OK: Installed/source hash parity for all upgraded skill files.
- OK: Generic anti-overfit and multi-domain Atlas checks.
- OK: Research audit helper smoke tests and Python compile checks.

### Findings
- Research workflow now includes a generic Research Reasoning Atlas stage with branch tree, debate matrix, alternative explanations, confounder ledger, model-lens selection, expert stance map, causal-chain questions, counterfactual traces, conclusion tournaments, and future falsifiers.
- SourceGuard now owns branch-aware source discovery, disconfirming-source priority, source-lineage checks, expert-stance sources, model sources, and branch-distinguishing evidence.
- TraceGuard now preserves competing storylines, causal-chain weak links, counterfactual uncertainty, confounders, and red-team storylines.
- LogicGuard now requires central conclusions to survive a conclusion tournament with steelman opposition, live alternatives, model-lens warrants, expert-role boundaries, robustness tests, and allowed wording.
- Installed Codex skill copies were synchronized from edited local source skill directories and hash-verified.

### Counterexamples
- Duplicate-boundary FlowGuard fixture remains blocked so the workflow cannot become a new all-in-one research engine.
- Stale-validation FlowGuard fixture remains blocked so installed-skill edits require fresh validation.
- Bad helper-script fixtures fail as expected for undefined source markers and missing source-role coverage.

### Friction Points
- The first nested PowerShell copy attempt did not synchronize every installed file; a direct per-file copy fixed the mismatch and full hash parity passed.
- `quick_validate.py` requires the skill directory argument.

### Skipped Steps
- No remote push, release publication, or git commit was performed.
- No standalone FlowGuard skill was changed; FlowGuard remains process/freshness/closure governance.

### Risk Evidence Summary
- The upgrade is intentionally generic: domain details must stay in selected model lenses, examples, or future lens packs, not core skill prompts.
- Branch volume alone is not treated as quality; quality gates require branch relevance, disconfirming evidence, source lineage, competing storylines, conclusion tournament status, and reader-facing wording boundaries.

## strengthen-research-source-and-citation-quality-20260602 - Source registry, execution-chain, and citation-quality hardening

- Project: ResearchInvestigationWorkflow_20260531
- Trigger reason: User requested OpenSpec + FlowGuard governed upgrade of research-investigation-workflow, SourceGuard, TraceGuard, and LogicGuard after comparing report quality with ChatGPT Deep Research
- Status: completed
- Skill decision: use_direct_flowguard_skill: existing_model_preflight plus development_process_flow; companion OpenSpec change strengthen-research-source-and-citation-quality
- Started: 2026-06-02T06:50:00+00:00
- Ended: 2026-06-02T07:13:16+00:00
- Commands OK: True

### Model Files
- .flowguard/existing_model_preflight/model.py
- .flowguard/development_process_flow/model.py

### Commands
- OK: `python -c "import flowguard; print(flowguard.SCHEMA_VERSION)"` -> schema 1.0
- OK: `python -c "import importlib.metadata as m; print(m.version('flowguard'))"` -> package 0.40.4
- OK: `python -m flowguard project-audit --root .` -> pass
- OK: `python .flowguard\existing_model_preflight\run_checks.py` -> valid route passed; duplicate-boundary fixture remains blocked as expected
- OK: `python .flowguard\development_process_flow\run_checks.py` -> valid lifecycle passed; stale-validation fixture remains blocked as expected
- OK: `openspec validate strengthen-research-source-and-citation-quality --strict`
- OK: installed skill `quick_validate.py` checks for research-investigation-workflow, SourceGuard, TraceGuard, traceguard-library, LogicGuard, logicguard-source-library, logicguard-structured-artifact, and logicguard-artifact-synthesis
- OK: SourceGuard, TraceGuard, and LogicGuard command-surface checks
- OK: citation marker and source-role coverage helper smoke tests with passing and failing fixtures
- OK: focused SourceGuard, TraceGuard, and LogicGuard example checks
- OK: installed/source hash parity check for all synchronized skill folders

### Findings
- Research workflow now requires a source registry, source-role coverage review, execution/evidence-chain status, citation consistency audit, and final research quality gate before strong closure claims.
- SourceGuard guidance now owns source-role coverage review and post-draft source-gap routing without turning candidates into proof.
- TraceGuard guidance now preserves announcement-to-execution chains, safe/unsafe wording, and source registry ids for high-impact leads.
- LogicGuard guidance now reconciles source registries, claim-to-source matrices, citation markers, source roles, and paragraph wording before final source-backed prose is treated as ready.
- Installed Codex skill copies were synchronized from the edited local source skill directories.

### Risk Evidence Summary
- Broken-route FlowGuard fixture still blocks a duplicate all-in-one research engine by design.
- Stale-lifecycle FlowGuard fixture still blocks stale validation evidence by design.
- The Markdown citation helper checks structural marker hygiene only; semantic source-role mismatch remains a LogicGuard audit responsibility.

### Skipped Steps
- No remote push, release publication, or git commit was performed.


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


## integrate-sourceguard-discovery-loop-20260531 - Integrate SourceGuard discovery planning into research-investigation-workflow and prepare v0.2.0 release

- Project: ResearchInvestigationWorkflow_20260531
- Trigger reason: Non-trivial skill/process upgrade with OpenSpec, installed skill sync, command-surface validation, GitHub release, and stale-evidence closure
- Status: completed
- Skill decision: use_direct_flowguard_skill: existing_model_preflight plus development_process_flow
- Started: 2026-05-31T20:39:23+00:00
- Ended: 2026-05-31T20:39:23+00:00
- Duration seconds: 0.000
- Commands OK: True

### Model Files
- .flowguard\existing_model_preflight\model.py
- .flowguard\development_process_flow\model.py

### Commands
- OK (0.000s): `openspec validate integrate-sourceguard-discovery-loop --strict`
- OK (0.000s): `python -m flowguard project-audit --root .`
- OK (0.000s): `python .flowguard\existing_model_preflight\run_checks.py`
- OK (0.000s): `python .flowguard\development_process_flow\run_checks.py`
- OK (0.000s): `quick_validate.py skills\research-investigation-workflow`
- OK (0.000s): `installed/project skill parity check`

### Findings
- SourceGuard now owns source-discovery planning while TraceGuard, LogicGuard, and FlowGuard retain separate boundaries

### Counterexamples
- none recorded

### Friction Points
- none recorded

### Skipped Steps
- none recorded

### Risk Evidence Summary
- Broken-route FlowGuard fixtures intentionally remain blocked for duplicate combined-engine and stale-validation scenarios

### Next Actions
- Publish v0.2.0 and archive OpenSpec change after release if desired

## strengthen-research-artifact-contract-20260601 - Strengthen research investigation artifact contract across Guard skills

- Project: ResearchInvestigationWorkflow_20260531
- Trigger reason: User requested OpenSpec and FlowGuard governed optimization after comparing local Guard-family research workflow with ChatGPT deep research behavior
- Status: completed
- Skill decision: use_direct_flowguard_skill: existing_model_preflight plus development_process_flow; companion OpenSpec change strengthen-research-artifact-contract
- Started: 2026-06-01T13:00:00+00:00
- Ended: 2026-06-01T13:05:00+00:00
- Commands OK: True

### Model Files
- .flowguard/existing_model_preflight/model.py
- .flowguard/development_process_flow/model.py

### Commands
- OK: `python -c "import flowguard; print(flowguard.SCHEMA_VERSION)"` -> schema 1.0
- OK: `python -m flowguard project-audit --root .`
- OK: `python .flowguard\existing_model_preflight\run_checks.py` -> valid route passed; built-in duplicate-boundary fixture remains blocked as expected
- OK: `python .flowguard\development_process_flow\run_checks.py` -> valid lifecycle passed; built-in stale-validation fixture remains blocked as expected
- OK: `openspec validate strengthen-research-artifact-contract --strict`
- OK: changed installed and source skill `quick_validate.py` checks
- OK: installed/source hash parity check

### Findings
- Research workflow now records requested final artifact genre and a research plan card before collecting evidence.
- The workflow now has a per-round replan gate and supports report, paper, memo, brief, article, literature review, deck storyline, and decision note outputs.
- Final output coverage obligations remain internal reasoning checks and do not force diagnostic headings into reader-facing prose.

### Risk Evidence Summary
- Broken-route fixture still blocks duplicate all-in-one engine ownership by design.
- Stale-lifecycle fixture still blocks old validation evidence by design.

### Skipped Steps
- No remote push or release publication was performed.


## flowguard-project-upgrade - FlowGuard project upgrade record update

- Project: ResearchInvestigationWorkflow_20260531
- Trigger reason: target project uses FlowGuard and needs durable AGENTS/version records
- Status: completed
- Skill decision: used_flowguard
- Started: 2026-06-02T06:50:35+00:00
- Ended: 2026-06-02T06:50:35+00:00
- Duration seconds: 0.000
- Commands OK: True

### Model Files
- none recorded

### Commands
- none recorded

### Findings
- FlowGuard repository recorded: https://github.com/liuyingxuvka/FlowGuard
- FlowGuard package version recorded: 0.40.4
- FlowGuard schema version recorded: 1.0
- Artifact upgrade scan: apply: scanned=2 upgraded=0 blocked=0 changed=0

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
