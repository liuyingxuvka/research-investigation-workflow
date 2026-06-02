# Research Reasoning Atlas

Use this reference for substantive research artifacts where the user expects reasoning depth beyond a linear source-backed report. The Atlas is a generic reasoning map. It must not encode a domain-specific checklist in the core workflow.

## Core Rule

Use transferable reasoning primitives:

```text
branch tree
debate matrix
alternative explanation matrix
confounder ledger
model lens selection
expert stance map
causal chain
counterfactual trace
conclusion tournament
future trigger and falsifier list
```

Do not hard-code topic-specific prompts in this file. Domain-specific details belong in optional lens packs, source plans, examples, or user-requested case notes.

## Branch Tree

For each important claim or question, record:

```text
branch id
branch type: support | oppose | alternative | confounder | scope | temporal | stakeholder | method | falsifier | future trigger
question answered
why it matters
current support
current opposition
needed evidence
claim impact: central | material | contextual | optional
final treatment: main text | limitation | appendix | follow-up | omit
```

Branch count is not the goal. Branches must matter to the conclusion, scope, method, or reader decision.

## Debate Matrix

For every central conclusion candidate:

```text
conclusion candidate
strongest support
strongest opposition
best alternative explanation
best limiting condition
current adjudication
missing evidence
allowed wording strength
```

The final artifact may still be concise, but the internal reasoning should know why the preferred conclusion beats, loses to, or is narrowed by alternatives.

## Model Lens Selection

Select analytical lenses only when they add work:

```text
lens id
lens type: causal | economic | institutional | technical | statistical | legal | behavioral | historical | risk | systems | comparative | domain-specific
why this lens fits
branch or warrant generated
evidence need generated
limitation generated
where it appears: reasoning only | appendix | final prose
```

A lens name is not evidence. It must create a warrant, branch, evidence requirement, limitation, or falsifier.

## Expert Stance Map

When expert or institutional interpretation matters, record:

```text
expert or institution
relevant expertise or role
stance family
stance type: fact evidence | interpretation | forecast | stakeholder statement | method lens | disputed claim | background
branch supported or opposed
evidence cited by the expert
potential limitation or interest boundary
final use
```

Expert opinion must not be treated as direct fact unless the expert source actually provides direct evidence.

## Causal And Counterfactual Reasoning

For claims involving cause, execution, impact, outcome, or change:

```text
proposed cause
intermediate mechanism
observed effect
alternative causes
confounders
counterfactual: what likely happens without the proposed cause
evidence for each link
weakest link
safe wording
```

If the effect could plausibly occur without the proposed cause, the conclusion must be qualified unless additional evidence distinguishes the cause.

## Conclusion Tournament

Before strong final conclusions:

```text
preferred conclusion
steelman opposition
alternative explanations
evidence comparison
warrant comparison
assumption load
scope fit
rebuttal status
robustness if strongest source is removed
robustness if strongest opposition is accepted
winner: preferred | alternative | unresolved | downgraded
final wording
```

This tournament is owned by LogicGuard, but the research workflow should require it for central claims in substantial artifacts.

## Reader Artifact Boundary

The Atlas is internal support material. The final artifact should use only what helps the reader:

- Put the clean conclusion and important limitations in the main text.
- Put detailed branch, expert, lens, counterfactual, and tournament material in an appendix or local run record when useful.
- Do not expose internal Guard-family labels unless the user asks for methodology.

## Anti-Overfit Rule

Core skill language should use generic categories:

```text
external drivers
alternative causes
scope boundaries
implementation signals
outcome signals
stakeholder impacts
source lineage
expert stance families
falsifying evidence
future triggers
```

If a proposed rule names a specific industry, topic, metric, technology, institution class, or causal factor, treat it as a domain lens or example, not as a core Atlas rule.
