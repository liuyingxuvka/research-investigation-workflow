## Context

`research-investigation-workflow` already requires deep logic-lead investigation, inline citations, TraceGuard handoff, LogicGuard synthesis, FlowGuard closure, and local-only outputs. The first real investigation run showed a narrower but important class of failure risk: policy rumors can sound like one event while actually mixing different evidence roles. For example, a local tax exemption, a central transaction-tax policy, weak market data, land-finance stress, and an expert quote can be collapsed into a false "national tax is coming" story unless the skill forces role separation.

## Goals / Non-Goals

**Goals:**

- Make policy-rumor and current-event investigations role-aware by default.
- Require implementation-signal checks before strong negative or positive findings.
- Improve report readability through reader routes, section handoffs, and paragraph jobs.
- Strengthen installed/source skill parity and software-only commit discipline.

**Non-Goals:**

- Do not create a new reasoning engine.
- Do not merge TraceGuard Case Library and LogicGuard Source Library.
- Do not modify standalone FlowGuard skill behavior.
- Do not commit local investigation reports, private ledgers, or source libraries to public software repositories.

## Decisions

1. Encode policy-rumor behavior in `research-investigation-workflow`, not FlowGuard.

   Rationale: FlowGuard owns process and freshness closure. Report-specific content rules belong in the orchestration skill and its references.

2. Strengthen child skills only where their existing role already applies.

   Rationale: TraceGuard should own event/implementation/evidence-chain separation; LogicGuard should own claim support, report structure, citation placement, and final audit. Neither child skill should become a replacement for the orchestration workflow.

3. Use text-level skill validation rather than adding runtime dependencies.

   Rationale: The upgraded surfaces are skill instructions and references. Targeted checks for required phrases, OpenSpec validation, FlowGuard audit, and file parity are the strongest proportional checks.

4. Keep local/private artifacts ignored.

   Rationale: The user explicitly separated software source from local reports and investigation history. This change preserves that boundary.

## Risks / Trade-offs

- [Risk] The extra policy-rumor ladder could make quick investigations longer.
  - Mitigation: Apply it to substantive policy/current-event rumor work; short direct answers can still summarize with explicit caveats.
- [Risk] Child skill guidance could duplicate the orchestration skill.
  - Mitigation: Add only role-specific instructions to TraceGuard and LogicGuard.
- [Risk] Installed skill sync can drift from source mirrors.
  - Mitigation: Validate source/installed parity after copying and record synced commit ids.
