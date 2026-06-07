# AGENTS.md

## Language

Use Chinese when communicating with the user.

## Project Purpose

This project prepares and implements a Codex skill named
`research-investigation-workflow`.

The skill orchestrates existing Guard-family workflows:

- TraceGuard for evidence-to-storyline reconstruction.
- LogicGuard for source preservation, argument modeling, report synthesis, and
  final claim audit.
- FlowGuard for staged workflow, evidence freshness, and closure safety.
- Research Investigation History Ledger for run-level reusable memory.

## Core Rule

Do not invent a new core reasoning engine. Build a thin orchestration skill that
reuses existing TraceGuard, LogicGuard, and FlowGuard capabilities.

## Required Preflight

Before non-trivial work:

1. Use predictive KB preflight.
2. Use skill-creator when creating or updating the actual skill.
3. Use FlowGuard routing for non-trivial skill, process, or validation work.
4. Check current TraceGuard, LogicGuard, and FlowGuard command surfaces before
   claiming the plan is implemented.

## Boundaries

- TraceGuard Case Library stores messy case evidence and search directions.
- LogicGuard Source Library stores durable formal source support.
- FlowGuard logs and models store process evidence, not investigation evidence.
- Research Investigation History Ledger stores run history and reusable workflow
  lessons, not factual proof.

## First Implementation Target

Create a skill folder named `research-investigation-workflow`, likely under:

```text
%USERPROFILE%\\.codex\\skills\research-investigation-workflow
```

Use this structure:

```text
research-investigation-workflow/
  SKILL.md
  agents/
    openai.yaml
  references/
    workflow.md
    evidence-source-policy.md
    traceguard-loop.md
    logicguard-report-synthesis.md
    flowguard-closure.md
    history-ledger.md
    output-contract.md
```

Do not add README, changelog, install guide, or broad docs inside the final
skill folder unless the user explicitly asks. Keep detailed material in
references.

<!-- BEGIN FLOWGUARD PROJECT RULES -->
## FlowGuard Project Rules

This project uses FlowGuard for non-trivial maintenance, feature work, bug
fixes, refactors, tests, release work, project upgrades, and evidence-sensitive
process changes.

FlowGuard repository:
https://github.com/liuyingxuvka/FlowGuard

Project FlowGuard record:
- Manifest: `.flowguard/project.toml`
- Machine log: `.flowguard/adoption_log.jsonl`
- Human log: `docs/flowguard_adoption_log.md`

Current adoption record:
- FlowGuard package version: `0.40.12`
- FlowGuard schema version: `1.0`

Before non-trivial work:
1. Verify the real package:
   `python -c "import flowguard; print(flowguard.SCHEMA_VERSION)"`
2. Check the installed package version:
   `python -c "import importlib.metadata as m; print(m.version('flowguard'))"`
3. Audit the project record:
   `python -m flowguard project-audit --root .`
4. Compare the installed version with `.flowguard/project.toml`.
5. If the installed version is newer, run:
   `python -m flowguard project-upgrade --root .`
   This updates the project record and scans existing FlowGuard artifacts,
   model evidence, tests, docs, and guidance for deterministic upgrades into
   the current FlowGuard shape. Use `--records-only` only when intentionally
   scoping out artifact/model/test upgrade scanning.
   Then rerun affected models/tests before broad confidence and record the result.
6. If the installed version is older than the project record, stop and upgrade
   the local FlowGuard toolchain before claiming FlowGuard confidence.

FlowGuard runtime guidance is latest-schema-first: old artifacts may be
detected and upgraded at project/tool boundaries, but normal route logic should
not preserve long-lived compatibility branches for obsolete fields, aliases, or
wrappers.

Default replacement means dispose the old path, old field, alias, wrapper, or
fallback unless compatibility or preservation is explicitly requested. If
compatibility is explicit, record the preserved surface, compatibility intent,
and current evidence; otherwise delete, block, migrate, delegate, repair, or
scope it out with a concrete reason.

Field-bearing work should use or update FieldLifecycleMesh: high-level behavior
models include behavior-bearing fields, while child/leaf field rows account all
discovered fields and record owner, readers, writers, projection, lifecycle,
and old-field disposition.

After non-trivial FlowGuard-managed work, run or record a maintenance scan when
changed artifacts, skipped routes, stale evidence, or split/reduction signals
may require an owning route such as Model-Test Alignment,
DevelopmentProcessFlow, Architecture Reduction, StructureMesh, ModelMesh,
TestMesh, or AgentWorkflowRehearsal.

Do not create a fake local FlowGuard replacement. Do not claim full FlowGuard
completion from an AGENTS/manifest/log update alone; executable model checks,
tests, replay, and closure evidence still need to be current for the claim.
<!-- END FLOWGUARD PROJECT RULES -->
