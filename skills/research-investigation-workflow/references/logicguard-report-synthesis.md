# LogicGuard Report Synthesis

Use LogicGuard after evidence has been organized enough to model claims, preserve important sources, synthesize a target artifact such as a report, paper, memo, brief, article, or deck storyline, attach inline citation markers, audit final prose, or adjudicate a Research Reasoning Atlas conclusion tournament. Use SourceGuard before promotion when the investigation still needs source-discovery planning, branch-aware search, missing-role search, or counter/limiting source search.

## Boundary

LogicGuard answers:

```text
Does the written conclusion follow from declared support?
```

It does not decide factual truth. It does not store messy case evidence. It does not replace TraceGuard contradiction review.

It also does not rank search actions. When a LogicGuard gap depends on missing evidence, send that gap back to SourceGuard unless the correct result is to downgrade or omit the claim.

LogicGuard is the final owner for claim-to-source consistency. It should check that inline markers, source registry entries, claim roles, limitations, and final prose treatment agree before the artifact is treated as passed.

LogicGuard is also the final owner for deciding whether a preferred conclusion is structurally stronger than steelman opposition and material alternatives. It checks support structure, not factual truth.

## Current Command Surface Check

Before relying on a specific command, check:

```powershell
python %USERPROFILE%\\.codex\\skills\logicguard\scripts\run_logicguard.py --help
```

Inspect subcommand help for the route being used.

## Promotion From SourceGuard Or TraceGuard

Promote a source only when it is:

- important to a final claim;
- stable enough for formal preservation;
- useful for future reports, papers, or audits;
- not merely a rejected search result, temporary clue, or weak signal.

Record the promotion explicitly:

- SourceGuard case/action id when the source came from a discovery plan;
- TraceGuard case id when the source has been used in a trace;
- source id or path;
- reason for promotion;
- source registry id or citation marker when one exists;
- LogicGuard library id or model path;
- claim or section it supports.

Do not bulk-promote SourceGuard candidate sources. A candidate source is eligible only after it is found, relevant, stable enough to cite or preserve, and tied to a source role in the claim-to-source matrix.

## Source Preservation

Use source-library or intake routes when durable support is needed:

```powershell
python %USERPROFILE%\\.codex\\skills\logicguard\scripts\run_logicguard.py intake ...
python %USERPROFILE%\\.codex\\skills\logicguard\scripts\run_logicguard.py library ...
```

Keep source chronology distinct:

- `added_at`: when the source entered the library;
- `source_date`: when the source itself is dated;
- `coverage_period`: what factual period the source covers.

## Argument Modeling

Model:

- root claims;
- supporting evidence;
- warrants or mechanisms;
- assumptions;
- rebuttals;
- limitations;
- scope;
- missing support.

For Atlas-driven work, also model:

- preferred conclusions;
- steelman opposing views;
- material alternative explanations;
- selected analytical lenses as warrants, scope rules, or limitations;
- expert stances as fact evidence, interpretation, forecast, stakeholder statement, method lens, disputed claim, or background;
- robustness checks and conclusion downgrades.

Run checks when available:

```powershell
python %USERPROFILE%\\.codex\\skills\logicguard\scripts\run_logicguard.py validate <model>
python %USERPROFILE%\\.codex\\skills\logicguard\scripts\run_logicguard.py evaluate <model>
python %USERPROFILE%\\.codex\\skills\logicguard\scripts\run_logicguard.py diagnose <model>
python %USERPROFILE%\\.codex\\skills\logicguard\scripts\run_logicguard.py gaps <model>
```

Deepen high-importance, weak, or reader-risk nodes before confident prose.

## Genre-Preserving Synthesis Boundary

The requested artifact genre controls final organization and tone. LogicGuard must not force a diagnostic-table style or fixed fact/official-claim/inference/gap headings into the reader-facing artifact.

Use source roles, claim types, limitations, and gaps as internal coverage obligations and audit dimensions. They may appear as natural prose, citations, footnotes, tables, or appendix depending on the requested artifact. The final artifact should read like the requested artifact, not like a model audit, while still keeping important claims traceable.

## Claim-To-Source Matrix

Before writing final artifact prose, build or inspect a claim-to-source matrix:

```text
claim id
lead id
target artifact locator: section | paragraph | page | slide | note | appendix
source ids
source registry ids or final citation markers
source role: event fact | official claim | independent report | limiting evidence | expert analysis | historical background | hypothesis | forecast trigger
source date or freshness
claim use: direct support | scope limiter | contrast | context | forecast trigger
claim strength
inline citation marker, such as [S1] or [S1; S4]
limitation or rebuttal
final prose treatment: main text | footnote | appendix | omitted with reason
```

Each important factual claim, official-claim report, analytic inference, limitation, and future hypothesis must have either an inline citation marker or an explicit note that it is uncited framing/background. Do not leave a key paragraph supported only by a final bibliography.

For all substantive investigation writing, the matrix must keep claim origin, direct facts, source statements, scope limits, execution or outcome evidence, context or motive evidence, expert interpretation, counter or limiting evidence, and forecast triggers separate. Interpretation or motive context can support plausibility, but cannot support a claim that execution, causality, outcome, or broader scope has been established.

The matrix must agree with the source registry. Treat these as audit failures:

- final prose uses `[S#]` with no matching source entry;
- two different source entries share the same final marker without an intentional merge;
- a source is used as direct support for a role it does not cover;
- execution, outcome, causality, or scope claims cite only announcement, context, motive, or interpretation sources;
- important limiting evidence is present in the registry but omitted from the paragraph it narrows.

## Conclusion Tournament

Before strong final conclusions, run or simulate a conclusion tournament:

```text
preferred conclusion
steelman opposition
material alternative explanations
strongest support
strongest opposition
selected model lenses and warrants
expert stance families
assumption load
scope fit
unanswered rebuttals
robustness if strongest source is removed
robustness if strongest opposition is accepted
winner: preferred | alternative | unresolved | downgraded
allowed final wording
```

If the preferred conclusion wins narrowly, use qualified wording. If the steelman opposition or an alternative explanation wins, downgrade, omit, or send the gap back to SourceGuard or TraceGuard.

Model lenses must do work. A selected lens should create a warrant, branch, evidence need, limitation, or falsifier. A decorative lens name is not a LogicGuard pass.

Expert stances must remain typed. Do not convert expert interpretation, forecast, stakeholder statement, or method commentary into direct fact evidence.

## Section And Paragraph Blueprint

Create a story plan before final prose. For core sections or artifact regions, include:

```text
section purpose
previous-section handoff
main claim
lead ids resolved
reader question answered
paragraph, page, slide, or artifact sequence
evidence and limiting evidence
required citation markers
next-section handoff
```

For core paragraphs or artifact units, include:

```text
paragraph/page/slide/unit job
claim sentence
support sentence(s)
limitation or counter sentence when relevant
who says it or which source role supports it
source markers
claim strength label
source-role label when ambiguity matters
final treatment: main text | footnote | appendix | omitted with reason
```

This blueprint is the bridge between LogicGuard modeling and readable target-artifact prose. If it is missing for a core section or artifact region, report the draft as under-modeled.

Before drafting each core paragraph, know:

```text
what this paragraph proves
which sentence is direct fact
which sentence is a source or actor claim
which sentence is expert interpretation
which sentence is the report's inference
which [S#] marker supports or limits each sentence
```

## Synthesis

Create a story plan or outline before final prose:

```powershell
python %USERPROFILE%\\.codex\\skills\logicguard\scripts\run_logicguard.py synthesize <model> --goal "<goal>" --profile report --delivery
```

Use the synthesized plan to write a readable target artifact. Do not expose every diagnostic detail in the reader-facing artifact, but keep source markers and claim-strength wording visible where they matter. Preserve the requested genre: report, paper, memo, brief, article, literature review, deck storyline, or another user-specified artifact.

Recommended prose pattern:

```text
Event fact from source [S1]. Official claim from source [S2]. Limiting or independent evidence from source [S3]. Therefore, qualified conclusion rather than overclaim.
```

Separate direct quotes, paraphrases, and synthesis:

- direct quote: short and attributed;
- paraphrase: source marker required;
- synthesis: multiple source markers and clear wording such as "taken together" or "the available evidence supports";
- hypothesis: label as candidate and cite why it is plausible plus what remains missing.

## Final Claim Audit

Audit final prose for:

- overclaiming;
- missing warrant;
- hidden assumption;
- unsupported causality;
- scope mismatch;
- unanswered rebuttal;
- missing limitation;
- candidate written as confirmed;
- hypothesis written as evidence;
- source existence written as source support.
- important claim without inline citation marker;
- official claim written as independent fact;
- interpretation, context, or motive evidence written as execution, causality, outcome, or broader-scope evidence;
- local or scope-limited evidence written as broader-scope evidence without a bridging source;
- limiting source omitted from a paragraph that relies on a contested claim;
- section order that lacks a clear reasoning handoff.
- internal Guard-family tool names leaked into the reader-facing artifact when no methods appendix was requested;
- missing "who says this" wording for paragraphs that combine source claims, evidence, and inference.
- final artifact reads like a diagnostic dump or tool log instead of the requested genre;
- required coverage categories appear as forced visible headings when they would damage the requested artifact.
- inline citation markers that do not resolve to the source registry;
- duplicate or ambiguous source ids;
- important source-registry entries used in prose without matching claim-to-source matrix rows;
- important final claims whose nearest citation supports only context, motive, announcement, or interpretation rather than the claim as written.
- preferred conclusions that did not face steelman opposition;
- live alternative explanations hidden from the final limitation or appendix;
- selected analytical lenses that are named but not used as warrants, limitations, or evidence needs;
- expert stance families treated as if they were all the same kind of support;
- robustness failures hidden behind polished prose.

Run this audit after the last material prose edit. If the report changes after audit, rerun the audit or mark the closure evidence stale.

When the final artifact is Markdown with compact `[S#]` markers, run the citation helper if available before closure:

```powershell
python %USERPROFILE%\\.codex\\skills\research-investigation-workflow\scripts\audit_markdown_sources.py <artifact.md> --json
```

The helper only catches structural marker problems. LogicGuard must still check semantic role mismatch, overclaiming, missing warrant, and missing limitation.

If audit fails, choose one:

```text
search more through SourceGuard
weaken the claim
move claim to hypothesis
move claim to unresolved gap
remove claim
```

Record the audit result in the appendix and History Ledger postflight.

## Final Research Quality Gate

Before claiming the artifact is complete, combine the LogicGuard audit with upstream evidence gates:

```text
source registry status
source-role coverage status from SourceGuard
TraceGuard evidence/execution-chain status
TraceGuard competing-storyline, causal-chain, counterfactual, and confounder status
Research Reasoning Atlas branch, model-lens, expert-stance, and debate status
claim-to-source matrix status
citation consistency status
conclusion tournament result
remaining argument gaps
allowed final claim strength
```

If the weakest important gate is partial or blocked, LogicGuard should recommend a targeted SourceGuard search, TraceGuard reconstruction pass, claim downgrade, or omission rather than polishing unsupported prose.
