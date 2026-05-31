# Implementation Roadmap

## Phase 1: Project Confirmation

Tasks:

- confirm final skill name: `research-investigation-workflow`;
- confirm target install location, likely `C:\Users\liu_y\.codex\skills`;
- confirm first version is a Codex skill, not a UI or standalone app;
- confirm the History Ledger root convention.

Expected decision:

```text
Build a thin orchestration skill first.
```

## Phase 2: Skill Skeleton

Use `skill-creator`.

Target structure:

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

Do not add README, changelog, or installation docs inside the actual skill
folder.

## Phase 3: Core Skill Instructions

`SKILL.md` should stay concise and say:

- when to trigger;
- required first steps;
- how to route to TraceGuard, LogicGuard, FlowGuard, and History Ledger;
- hard boundaries;
- final output contract.

It should not contain every detail. Put detailed procedures in references.

## Phase 4: Reference Files

Write references:

- `workflow.md`: end-to-end investigation loop.
- `evidence-source-policy.md`: public, local, internal, access-gap, hypothesis.
- `traceguard-loop.md`: Case Library and gap-driven TraceGuard work.
- `logicguard-report-synthesis.md`: formal source promotion, report synthesis,
  final claim audit.
- `flowguard-closure.md`: staged process, stale evidence, closure.
- `history-ledger.md`: preflight and postflight run history.
- `output-contract.md`: final report and appendix requirements.

## Phase 5: Validation

Run skill validation:

```powershell
python C:\Users\liu_y\.codex\skills\.system\skill-creator\scripts\quick_validate.py C:\Users\liu_y\.codex\skills\research-investigation-workflow
```

Then do a manual smoke test with a fake investigation prompt:

```text
Use research-investigation-workflow to plan an investigation of a fictional API incident.
```

Check that the skill:

- starts from history preflight;
- asks or infers evidence access policy;
- routes messy material to TraceGuard;
- routes formal sources to LogicGuard only after promotion;
- reserves FlowGuard for process closure;
- outputs a human-readable report plus appendix plan;
- writes a history postflight record.

## Phase 6: Optional Scripts Later

Do not add scripts in version 1 unless needed.

Possible later scripts:

- initialize History Ledger;
- search History Ledger;
- append run records;
- produce a final run summary.

Only add these after the file format stabilizes.

