# Guard-Family Basis

This project must stay grounded in the existing Guard-family workflows.

## TraceGuard Existing Basis

TraceGuard currently supports:

- model validation;
- evaluation;
- diagnostics;
- gap ledger output;
- report output;
- LogicGuard bundle export;
- simulation;
- lightweight Case Library.

Relevant command surface:

```powershell
python -m traceguard validate <model.yaml>
python -m traceguard evaluate <model.yaml> --pretty
python -m traceguard diagnose <model.yaml> --pretty
python -m traceguard gaps <model.yaml> --pretty
python -m traceguard report <model.yaml> --format markdown
python -m traceguard export-logicguard <model.yaml> --output trace_logicguard_bundle.yaml
python -m traceguard library init <library-root>
python -m traceguard library create-case <library-root> <case-id>
python -m traceguard library add-direction <library-root> <case-id> <direction-id>
python -m traceguard library add-source <library-root> <case-id> <direction-id>
python -m traceguard library add-evidence <library-root> <case-id> <direction-id>
python -m traceguard library build-model <library-root> <case-id> --output <model.yaml>
python -m traceguard library write-back-gaps <library-root> <case-id> --result <evaluation.json>
```

TraceGuard boundary:

```text
TraceGuard reconstructs evidence-backed storylines.
It does not write final claims as truth.
```

## LogicGuard Existing Basis

LogicGuard currently supports:

- source intake and source-library preservation;
- argument model validation and evaluation;
- diagnostics;
- gap ledgers;
- structure mapping and audits;
- model deepening;
- artifact synthesis;
- final claim audit and rewrite suggestions.

Relevant command surface:

```powershell
python C:\Users\liu_y\.codex\skills\logicguard\scripts\run_logicguard.py intake ...
python C:\Users\liu_y\.codex\skills\logicguard\scripts\run_logicguard.py library ...
python C:\Users\liu_y\.codex\skills\logicguard\scripts\run_logicguard.py validate <model>
python C:\Users\liu_y\.codex\skills\logicguard\scripts\run_logicguard.py evaluate <model>
python C:\Users\liu_y\.codex\skills\logicguard\scripts\run_logicguard.py diagnose <model>
python C:\Users\liu_y\.codex\skills\logicguard\scripts\run_logicguard.py gaps <model>
python C:\Users\liu_y\.codex\skills\logicguard\scripts\run_logicguard.py structure audit <model>
python C:\Users\liu_y\.codex\skills\logicguard\scripts\run_logicguard.py synthesize <model> --goal "<goal>" --profile report --delivery
```

LogicGuard boundary:

```text
LogicGuard audits whether a claim is structurally licensed by declared support.
It does not decide factual truth.
```

## FlowGuard Existing Basis

FlowGuard currently supports:

- staged development/process models;
- evidence freshness;
- validation requirements;
- stale evidence detection;
- closure safety.

Relevant current TraceGuard project checks:

```powershell
python -c "import flowguard; print(flowguard.SCHEMA_VERSION)"
python -c "import importlib.metadata as m; print(m.version('flowguard'))"
python -m flowguard project-audit --root .
python .flowguard\development_process_flow\run_checks.py
```

FlowGuard boundary:

```text
FlowGuard guards process state and evidence freshness.
It does not reconstruct storylines or audit factual claims.
```

## Combined Boundary

Use this mental model:

```text
TraceGuard answers: What story does the evidence support?
LogicGuard answers: Does the written conclusion follow from the support?
FlowGuard answers: Was the process current, ordered, and honestly closed?
History Ledger answers: Have we done similar work before, and what did we learn?
```

