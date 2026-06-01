# Output Contract

Use this contract before final delivery. The final artifact should follow the user's requested genre; the appendix or support material should carry evidence, audit, and process details when useful.

## Main Artifact

The final artifact may be a research report, paper, memo, brief, article, literature review, deck storyline, decision note, or another research-backed artifact requested by the user. Include, when relevant to that genre:

- title;
- executive summary, abstract, thesis, brief answer, or equivalent opening;
- reader route for long artifacts: first question answered, why the next section follows, where limitations and future hypotheses appear;
- key findings;
- timeline or storyline;
- explanation of confidence and evidence levels;
- impact or implications;
- recommended next steps.

Write in human-readable artifact-native prose. Do not make the final artifact a diagnostic dump or Guard-family process log.

The reader-facing final artifact should not expose internal Guard-family tool names such as `SourceGuard`, `TraceGuard`, `LogicGuard`, `FlowGuard`, or `History Ledger` unless the user explicitly asked for a methods appendix. Use ordinary artifact-appropriate language instead: source search plan, event chain, evidence chain, argument structure, process check, source appendix, and run notes.

Important claims in the final artifact must carry compact inline source markers such as `[S1]`, `[S2; S5]`, or `[S3, limiting]`, or another citation form appropriate to the requested artifact. Do not rely on a final bibliography alone for source-backed claims.

Each important paragraph should make the source role clear when ambiguity matters:

- event fact;
- official claim;
- independent report;
- limiting or counter evidence;
- expert analysis;
- historical background;
- hypothesis or inference;
- forecast or future trigger.

Use a brief reader route near the start of long artifacts: what question is answered first, why the next section follows, and where limitations appear.

For every substantive final artifact, explicitly separate claim origin, direct facts, source statements, scope limits, execution or outcome evidence, context or motive evidence, expert interpretation, counter or limiting evidence, and forecast triggers in the underlying reasoning. Do not force these categories into visible headings unless that improves the requested artifact. Do not let context, motive, or expert interpretation stand in for execution, causality, outcome, or broader-scope evidence.

If the official/original fact, counter/limiting, impact/execution, stakeholder, or future-trigger rounds were not completed, title and close the output as an initial investigation, staged artifact, qualified finding, or downgraded conclusion rather than a complete or conclusive artifact.

## Evidence Levels

Use clear labels:

- `confirmed by cited evidence`;
- `supported but incomplete`;
- `candidate / working hypothesis`;
- `contradicted or disputed`;
- `access gap`;
- `not supported`.

Do not equate a numeric score with truth.

## Required Report Tables

For substantial final artifacts, include or append:

- logic-lead coverage table: lead, status, support, limiting evidence, gap, report treatment;
- source-discovery coverage table: source role, search action, result, access status, follow-up, claim impact;
- event/evidence timeline: date, event, source markers, confidence, relevance;
- claim-to-source matrix: important claim, artifact locator such as paragraph, section, page, or slide, source markers, source role, source date/freshness, claim use, limitation, final treatment;
- unresolved gap/watchlist table.

If a table is omitted, state why it would not add value for the current artifact.

## Appendix

Include:

- evidence-source policy summary;
- source-discovery plan, completed search actions, access gaps, and candidate-source downgrade notes;
- source appendix;
- logic-lead coverage summary;
- claim-to-source matrix;
- TraceGuard case and model summary;
- TraceGuard gaps and contradictions;
- LogicGuard source promotion summary;
- LogicGuard argument/audit summary;
- FlowGuard closure summary;
- hypothesis and assumption ledger;
- unresolved gaps;
- History Ledger postflight status.

## Wording Rules

Use strong wording only when evidence and audit support it:

- Strong: "The evidence shows..."
- Moderate: "The available evidence supports..."
- Provisional: "A plausible working hypothesis is..."
- Gap-aware: "The available record does not establish..."
- Contradiction-aware: "The sources conflict on..."
- Source-role aware: "The official source claims..."
- Execution-aware: "The available execution evidence does not yet show..."

Avoid:

- "proves" unless proof standards are explicit and met;
- "clearly" when support is partial;
- presenting a source's existence as support for its contents;
- presenting a search failure as evidence of absence unless search coverage supports that inference.
- placing citations only in the bibliography when a paragraph makes source-backed claims;
- writing official claims as independent facts;
- hiding limiting evidence in an appendix when it materially narrows a main finding or artifact thesis;
- writing inference, interpretation, or source commentary as established fact;
- omitting source-role wording when the reader needs to know who says the point;
- leaking internal workflow terms into the reader-facing final artifact;
- using a section, paragraph, page, or slide order that reads like a process log rather than the requested artifact.

## Closure Statement

End the appendix with:

```text
Closure status: passed | partial | blocked | downgraded
Current claim strength:
Inline citation coverage:
Logic-lead coverage:
Stale or skipped checks:
Unresolved gaps:
History Ledger postflight:
```

If blocked, include what is blocked, why it is blocked, the default next action, and what claim strength remains supportable.
