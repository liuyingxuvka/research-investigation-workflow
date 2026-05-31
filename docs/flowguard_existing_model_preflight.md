# FlowGuard Existing Model Preflight Notes

Use this scaffold before discussing, proposing, or implementing a non-trivial
change in an existing modeled system.

## What Existing Model Preflight Reviews

- which existing FlowGuard models were searched;
- which model responsibilities, FunctionBlocks, state fields, side effects,
  and public entrypoints already own the requested behavior;
- whether the change should reuse an existing boundary, extend an existing
  model, add a child model, or create a new boundary;
- whether duplicate model, state, side-effect, entrypoint, or responsibility
  ownership is resolved before downstream work starts;
- which downstream FlowGuard route should handle the concrete work.

Use a light grounding note for discussion and early analysis. Use a full
structured preflight before implementation, OpenSpec proposals, major
architecture changes, or risky behavior changes.
