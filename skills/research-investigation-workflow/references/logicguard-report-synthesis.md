# LogicGuard Report Synthesis

Use LogicGuard after evidence has been organized enough to model claims, preserve important sources, synthesize a report, or audit final prose.

## Boundary

LogicGuard answers:

```text
Does the written conclusion follow from declared support?
```

It does not decide factual truth. It does not store messy case evidence. It does not replace TraceGuard contradiction review.

## Current Command Surface Check

Before relying on a specific command, check:

```powershell
python C:\Users\liu_y\.codex\skills\logicguard\scripts\run_logicguard.py --help
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
python C:\Users\liu_y\.codex\skills\logicguard\scripts\run_logicguard.py intake ...
python C:\Users\liu_y\.codex\skills\logicguard\scripts\run_logicguard.py library ...
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
python C:\Users\liu_y\.codex\skills\logicguard\scripts\run_logicguard.py validate <model>
python C:\Users\liu_y\.codex\skills\logicguard\scripts\run_logicguard.py evaluate <model>
python C:\Users\liu_y\.codex\skills\logicguard\scripts\run_logicguard.py diagnose <model>
python C:\Users\liu_y\.codex\skills\logicguard\scripts\run_logicguard.py gaps <model>
```

Deepen high-importance, weak, or reader-risk nodes before confident prose.

## Synthesis

Create a story plan or outline before final prose:

```powershell
python C:\Users\liu_y\.codex\skills\logicguard\scripts\run_logicguard.py synthesize <model> --goal "<goal>" --profile report --delivery
```

Use the synthesized plan to write a readable report. Do not expose every diagnostic detail in the main report.

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

If audit fails, choose one:

```text
search more
weaken the claim
move claim to hypothesis
move claim to unresolved gap
remove claim
```

Record the audit result in the appendix and History Ledger postflight.
