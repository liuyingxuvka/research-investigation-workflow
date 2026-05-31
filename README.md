# Research Investigation Workflow

This project captures the plan for a new Codex skill named
`research-investigation-workflow`.

The skill should orchestrate existing Guard-family capabilities for long-running
research and investigation work:

```text
TraceGuard = reconstruct evidence-backed timelines and storylines.
LogicGuard = audit claims and synthesize readable reports from modeled support.
FlowGuard = guard process order, evidence freshness, and closure confidence.
```

This project is planning-first. It should not invent a new reasoning engine.
The first implementation should be a thin orchestration skill that reuses the
existing TraceGuard, LogicGuard, and FlowGuard workflows.

## Project Location

```text
C:\Users\liu_y\Documents\ResearchInvestigationWorkflow_20260531
```

## What To Read First

1. `PLAN.md` for the full landing plan.
2. `docs/guard-family-basis.md` for the existing capabilities this plan is based on.
3. `docs/history-ledger.md` for the new workflow history database idea.
4. `docs/implementation-roadmap.md` for the build order.
5. `NEXT_DIALOG_PROMPT.md` for starting a fresh Codex conversation.

## Core Product Definition

`research-investigation-workflow` is a research and investigation orchestration
skill. It helps Codex run multi-round investigations by:

- checking prior similar investigation runs;
- defining the investigation target and evidence policy;
- collecting public, local, and internal evidence where allowed;
- saving messy evidence into TraceGuard Case Library;
- using TraceGuard to build storylines, gaps, contradictions, and claim boundaries;
- using LogicGuard to preserve formal sources, deepen the argument, synthesize
  a readable report, and audit final claims;
- using FlowGuard to guard process state, revalidation, stale evidence, and final
  closure;
- writing a workflow history record after each run.

## Non-Goals

- Do not replace TraceGuard, LogicGuard, or FlowGuard.
- Do not merge TraceGuard Case Library into LogicGuard Source Library.
- Do not treat workflow history as evidence.
- Do not turn saved sources into final claims.
- Do not generate confident prose from missing evidence.
- Do not build a UI or database server in the first version.

