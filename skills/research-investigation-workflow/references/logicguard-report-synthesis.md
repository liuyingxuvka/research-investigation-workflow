# LogicGuard Report Synthesis

Use LogicGuard after evidence has been organized enough to model claims, preserve important sources, synthesize a report, attach inline citation markers, or audit final prose.

## Boundary

LogicGuard answers:

```text
Does the written conclusion follow from declared support?
```

It does not decide factual truth. It does not store messy case evidence. It does not replace TraceGuard contradiction review.

## Current Command Surface Check

Before relying on a specific command, check:

```powershell
python %USERPROFILE%\\.codex\\skills\logicguard\scripts\run_logicguard.py --help
```

Inspect subcommand help for the route being used.

## Promotion From TraceGuard

Promote a source only when it is:

- important to a final claim;
- stable enough for formal preservation;
- useful for future reports, papers, or audits;
- not merely a rejected search result, temporary clue, or weak signal.

Record the promotion explicitly:

- TraceGuard case id;
- source id or path;
- reason for promotion;
- LogicGuard library id or model path;
- claim or section it supports.

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

Run checks when available:

```powershell
python %USERPROFILE%\\.codex\\skills\logicguard\scripts\run_logicguard.py validate <model>
python %USERPROFILE%\\.codex\\skills\logicguard\scripts\run_logicguard.py evaluate <model>
python %USERPROFILE%\\.codex\\skills\logicguard\scripts\run_logicguard.py diagnose <model>
python %USERPROFILE%\\.codex\\skills\logicguard\scripts\run_logicguard.py gaps <model>
```

Deepen high-importance, weak, or reader-risk nodes before confident prose.

## Claim-To-Source Matrix

Before writing final report prose, build or inspect a claim-to-source matrix:

```text
claim id
lead id
section or paragraph target
source ids
source role: event fact | official claim | independent report | limiting evidence | expert analysis | historical background | hypothesis | forecast trigger
source date or freshness
claim use: direct support | scope limiter | contrast | context | forecast trigger
claim strength
inline citation marker, such as [S1] or [S1; S4]
limitation or rebuttal
```

Each important factual claim, official-claim report, analytic inference, limitation, and future hypothesis must have either an inline citation marker or an explicit note that it is uncited framing/background. Do not leave a key paragraph supported only by a final bibliography.

For policy-rumor or current-event writing, the matrix must keep official action, jurisdiction/scope, implementation evidence, fiscal or motive context, expert commentary, and forecast separate. Expert commentary or fiscal pressure can support plausibility or motive, but cannot support a claim that implementation has occurred.

## Section And Paragraph Blueprint

Create a story plan before final prose. For core sections, include:

```text
section purpose
previous-section handoff
main claim
lead ids resolved
reader question answered
paragraph sequence
evidence and limiting evidence
required citation markers
next-section handoff
```

For core paragraphs, include:

```text
paragraph job
claim sentence
support sentence(s)
limitation or counter sentence when relevant
source markers
claim strength label
source-role label when ambiguity matters
```

This blueprint is the bridge between LogicGuard modeling and readable prose. If it is missing for a core section, report the draft as under-modeled.

## Synthesis

Create a story plan or outline before final prose:

```powershell
python %USERPROFILE%\\.codex\\skills\logicguard\scripts\run_logicguard.py synthesize <model> --goal "<goal>" --profile report --delivery
```

Use the synthesized plan to write a readable report. Do not expose every diagnostic detail in the main report, but keep source markers and claim-strength wording visible where they matter.

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
- expert commentary, fiscal pressure, or motive context written as implementation evidence;
- local pilot action written as national rollout evidence without a bridging source;
- limiting source omitted from a paragraph that relies on a contested claim;
- section order that lacks a clear reasoning handoff.

Run this audit after the last material prose edit. If the report changes after audit, rerun the audit or mark the closure evidence stale.

If audit fails, choose one:

```text
search more
weaken the claim
move claim to hypothesis
move claim to unresolved gap
remove claim
```

Record the audit result in the appendix and History Ledger postflight.
