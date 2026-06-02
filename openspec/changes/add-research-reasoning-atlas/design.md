## Context

The current Guard-family research workflow already separates source discovery, trace reconstruction, argument audit, final citation consistency, and closure quality. The next quality gap is not source volume; it is breadth and depth of reasoning. A high-quality research run should expose many plausible branches, strong opposing interpretations, alternative explanations, transferable analytical lenses, expert stance groups, counterfactuals, and a final conclusion comparison.

The upgrade must remain generic. Prior AI data center and electricity-price work is useful as a regression prompt, but the workflow must not encode energy, weather, grid, finance, medicine, policy, or any other domain-specific checklist into the core skills.

## Goals / Non-Goals

**Goals:**

- Add a generic Research Reasoning Atlas layer on top of the existing SourceGuard, TraceGuard, and LogicGuard division of responsibilities.
- Make branch explosion, opposing views, alternatives, confounders, model lenses, expert stances, counterfactuals, and conclusion tournaments first-class workflow concepts.
- Preserve thin orchestration: research-investigation-workflow coordinates, SourceGuard discovers sources, TraceGuard reconstructs story/causal traces, and LogicGuard audits argument strength.
- Keep domain-specific content in optional lens packs, examples, or test prompts rather than in main skill rules.
- Sync source skill copies, installed skill copies, version metadata, changelogs, OpenSpec evidence, FlowGuard evidence, and validation results.

**Non-Goals:**

- Do not create a new core reasoning engine.
- Do not hard-code energy, electricity, weather, data-center, finance, medical, policy, company-strategy, or other domain checklists into the main skills.
- Do not require every final user-facing artifact to display internal Atlas tables.
- Do not replace SourceGuard, TraceGuard, or LogicGuard with a combined all-in-one workflow.
- Do not treat more branches as automatically better; branch quality and decision relevance matter.

## Decisions

### Decision 1: Add Generic Atlas Primitives, Not Domain Checklists

Use generic primitives:

- `branch_tree`
- `debate_matrix`
- `alternative_explanation_matrix`
- `confounder_ledger`
- `model_lens_selection`
- `expert_stance_map`
- `causal_chain`
- `counterfactual_trace`
- `conclusion_tournament`

Rationale: these apply across policy, markets, science, technology, medicine, company strategy, history, and incident review. Domain details belong in optional future lens packs.

Alternative considered: add detailed domain examples directly into SKILL.md. Rejected because it would overfit the skills to the current AI/electricity benchmark and reduce generality.

### Decision 2: Keep Ownership Split Across Existing Guards

- `research-investigation-workflow` owns Atlas stage order, output contract, and generic quality gates.
- SourceGuard owns branch-aware search planning, disconfirming-source priority, source diversity, source lineage, and model/expert source discovery.
- TraceGuard owns competing storylines, causal-chain state, counterfactual traces, confounder ledgers, and red-team storylines.
- LogicGuard owns conclusion tournaments, steelman opposing views, model lenses as warrants, expert claims as typed support, and robustness/stress tests.

Rationale: this respects existing tool boundaries and prevents a duplicate all-in-one research engine.

### Decision 3: Separate Internal Atlas From Reader-Facing Artifact

The Atlas is an internal research map and optional appendix. The final report, memo, paper, article, deck storyline, or decision note should remain artifact-native and readable.

Rationale: Deep internal reasoning should improve the artifact without turning every report into a diagnostic dump.

### Decision 4: Require Generic Anti-Overfit Language

Skill text should use abstract prompts such as "external drivers", "alternative causes", "scope boundaries", "implementation signals", "stakeholder impacts", and "falsifying evidence". It should avoid direct domain prompts such as "natural gas prices" unless inside an explicitly labeled example or future domain-lens reference.

Rationale: The user explicitly wants a universal upgrade for all future research.

## Risks / Trade-offs

- **Risk: Branch explosion creates noise instead of insight** → Mitigation: require relevance labels, claim impact, pruning criteria, and final treatment for each branch.
- **Risk: Model lenses become decorative names** → Mitigation: require each selected lens to generate a warrant, branch, evidence need, or limitation.
- **Risk: Expert quotes are treated as facts** → Mitigation: expert stances must be typed as fact evidence, interpretation, forecast, stakeholder statement, method lens, or disputed claim.
- **Risk: The workflow becomes too verbose for small tasks** → Mitigation: apply full Atlas obligations only to substantive/deep final artifacts; small answers can use a reduced Atlas.
- **Risk: Domain overfitting creeps in through examples** → Mitigation: keep domain examples out of core SKILL.md when possible and validate against multiple unrelated topic classes.
- **Risk: Installed skill copies drift from source repositories** → Mitigation: perform installed/source hash parity checks after sync.
