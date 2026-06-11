## Overview

Strengthen the orchestration prompt rather than adding another research engine.
The existing aggregate closure helper remains the executable gate; the skill
now states the ledger rows that must exist before that helper can support a
complete research claim.

## Decisions

- Use existing closure report fields: `closure_status`, `missing_inputs`,
  `stale_evidence`, `skipped_checks`, `next_actions`, `safe_claim`, and
  `unsafe_claim_boundary`.
- Add child Guard rows to the skill instructions, not to every child Guard
  skill.
- Keep research output genre-adaptive and avoid exposing internal Guard-family
  terms to readers unless the user asks for a methods appendix.

## Non-Goals

- Do not rewrite SourceGuard, TraceGuard, or LogicGuard.
- Do not add numeric weights.
- Do not replace source, trace, or argument judgment with row counting.
