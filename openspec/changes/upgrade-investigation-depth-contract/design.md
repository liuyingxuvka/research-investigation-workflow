## Context

`research-investigation-workflow` is intentionally a thin orchestration skill. It must reuse TraceGuard for messy evidence and storylines, LogicGuard for source-backed argument/report structure, and FlowGuard for process freshness and closure. The first real run proved the route can work, but it also exposed shallow report depth: the final report lacked inline claim citations, did not visibly exhaust the major logic leads, and treated report structure as a post-write audit instead of a pre-write plan.

The user clarified two architectural constraints:

- Investigation depth must be measured by logic-lead and evidence-chain coverage, not source counts or shallow/medium/deep modes.
- FlowGuard itself should not be changed for report-writing needs; only this orchestration skill should define how FlowGuard is used for investigation closure.

## Goals / Non-Goals

**Goals:**

- Make deep, lead-driven investigation the default behavior of `research-investigation-workflow`.
- Use a general evidence-role map instead of a policy-specific ladder.
- Require five minimum investigation rounds for substantive reports and downgrade closure when a round is incomplete.
- Require each important logic lead to have support, counter/support-limiting evidence, gap status, and report eligibility before final writing.
- Strengthen TraceGuard guidance so it produces a lead map, event chain, evidence-chain state table, and gap-driven follow-up search plan.
- Strengthen LogicGuard guidance so final reports use claim-to-source matrices, paragraph/section blueprints, inline citation markers, source-role labels, and final prose audit after the last text change.
- Add a `research-investigation-workflow` closure checklist that uses FlowGuard for workflow/freshness/privacy without altering FlowGuard's generic skill.
- Add reader-report cleanup so internal Guard-family terms do not leak into the main report unless the user requests a methods appendix.
- Keep local investigation outputs out of Git/GitHub by default.

**Non-Goals:**

- Do not create a new reasoning engine or merge Guard-family libraries.
- Do not modify FlowGuard's standalone skill behavior for research reports.
- Do not require a fixed minimum number of sources.
- Do not publish generated investigation reports, case libraries, source libraries, or ledgers as repository assets by default.

## Decisions

1. **Use logic-lead coverage and round completion instead of source-count depth.**  
   Rationale: A report can cite many weak or redundant sources and still miss the real explanation. The orchestrator should ask which causal, actor, outcome, contradiction, and future-impact lines remain unexplored.

2. **Generalize the evidence-role map.**  
   Rationale: The prior policy-rumor repair was directionally right but too narrow. Claim origin, direct fact, scope, execution, context, interpretation, counterevidence, and future trigger are reusable roles across investigations.

3. **Make TraceGuard own lead/evidence state, not prose quality.**  
   Rationale: TraceGuard already owns source-to-evidence-to-event-to-trace state. Extending its guidance to include lead maps and evidence-chain states fits its boundary without making it a report writer.

4. **Make LogicGuard own report blueprints and inline citation discipline.**  
   Rationale: LogicGuard's existing deep modeling contract already requires section plans, paragraph blueprints, evidence, warrants, assumptions, rebuttals, limitations, and scope. Citation-grounded writing is a natural extension of that contract.

5. **Keep FlowGuard generic and use it through a research-specific closure checklist.**  
   Rationale: FlowGuard answers whether the process is ordered, current, and honestly closed. The investigation skill should define which research artifacts and checks FlowGuard must consider.

6. **Clean reader-facing prose separately from method evidence.**  
   Rationale: Users need a report, not a tool log. Internal terms can stay in appendices and local ledgers, while the main report should use ordinary evidence and argument language.

7. **Sync installed and local source mirrors explicitly.**  
   Rationale: Installed skill folders are not always Git source roots. Each upgraded skill must be checked for installed path, source mirror, local repository status, validation, and committed software-only diffs.

## Risks / Trade-offs

- **Risk: More required intermediate artifacts may slow small investigations.**  
  Mitigation: Keep artifacts lightweight and proportional, but do not weaken the default deep-investigation contract.

- **Risk: Inline citations can clutter prose.**  
  Mitigation: Use compact `[S#]` markers and keep detailed source metadata in an appendix/source ledger.

- **Risk: LogicGuard structured audit may still report generic heading handoff warnings.**  
  Mitigation: Require a pre-write story plan and explicit section bridges, then treat remaining parser-granularity warnings separately from unsupported-claim diagnostics.

- **Risk: Installed skill updates may drift from repo mirrors.**  
  Mitigation: Validate hashes or diffs between installed and local mirrors for every upgraded skill and commit only source changes.

## Migration Plan

1. Update `research-investigation-workflow` SKILL and references in the project copy.
2. Update installed `research-investigation-workflow` to match the project copy.
3. Update TraceGuard source repo and installed TraceGuard skill guidance for lead/evidence-chain output.
4. Update LogicGuard source repo and installed LogicGuard/satellite guidance for citation-grounded deep report writing.
5. Do not modify FlowGuard skill. Update only `research-investigation-workflow/references/flowguard-closure.md`.
6. Run validation: quick skill validation, OpenSpec strict validation, command-surface checks, FlowGuard project audit, targeted text checks, and Git status.
7. Commit software-only changes in affected Git repositories.
