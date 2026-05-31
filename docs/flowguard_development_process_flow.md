# FlowGuard DevelopmentProcessFlow Notes

Use this scaffold to model a development lifecycle as a stateful process.

## What DevelopmentProcessFlow Reviews

- versioned requirements, designs, models, code, tests, docs, release assets,
  adapters, and sibling route report artifacts;
- ordered development actions that read, write, invalidate, or claim evidence;
- validation evidence and the exact artifact versions it covers;
- verifier changes, such as tests or model files changing after evidence was
  produced;
- freshness rules that propagate upstream changes to downstream artifacts;
- automatic ModelMesh/TestMesh split triggers for direct evidence that is
  oversized, incomplete, slow, broad, progress-only, or release-only;
- whether done, release, archive, or publish claims have current evidence;
- the minimum revalidation needed when evidence is stale or missing.

## Sibling Route Boundary

This is a sibling sub-protocol. It can reference evidence produced by ModelMesh,
TestMesh, StructureMesh, Model-Test Alignment, LongCheck, or Conformance
Adoption through evidence ids and freshness metadata. It does not inspect,
supervise, replace, or repair those routes. If sibling evidence is failed,
stale, skipped, missing, or progress-only, this route keeps that lifecycle gap
visible for the current process claim.

When direct model/test evidence reports state counts, pending budgeted states,
long durations, broad obligation coverage, background progress-only status, or
release-only scope, call `review_auto_mesh_splits()` and consume the resulting
ModelMesh or TestMesh gate before claiming broad parent confidence.

Use this route when development ordering, artifact overwrite, verification
freshness, or release readiness is the risk. It is not mandatory for every
small edit and it does not make FlowGuard a task orchestrator.
