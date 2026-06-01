# SourceGuard Discovery Loop

Use SourceGuard as the default source-discovery planner for substantive investigation work. It decides what to search next, why that source class matters, what gap it may close, and how to record the result before TraceGuard or LogicGuard receives it.

## Boundary

SourceGuard answers:

```text
What source or anchor should be searched next?
```

It does not answer whether a claim is true. Its utility score ranks search value, not factual confidence. A source candidate is not evidence. An evidence anchor is not an event. A search hit is not a final claim.

## Default Loop

```text
goal and evidence policy
-> SourceGuard belief state
-> ranked search actions
-> execute allowed public/local/internal searches with available tools
-> record observations as candidate sources and anchors
-> update SourceGuard gaps and frontier
-> hand candidate material to TraceGuard or LogicGuard only when ready
```

Run this loop before first-round search and again whenever TraceGuard, LogicGuard, or the user identifies an important missing source role.

## Build The Belief State

Record:

- research target and desired claim strength;
- leads and hypotheses;
- known source candidates;
- evidence anchors with exact locators when available;
- gaps, contradictions, source roles, and modalities;
- source policy: public, local, internal, permission-gated, unavailable, or unknown;
- planned search actions and utility reasons.

Use conservative defaults. Missing fields do not become high confidence.

## Search Policy Mapping

| Source class | Allowed action | Required handling |
| --- | --- | --- |
| Public web, public reports, papers, records | Use web/search/browser tools when available | Preserve title, URL, date, publisher, role, access date, and anchor locator |
| Local files, notes, downloaded PDFs, logs | Use local file search only within allowed scope | Preserve path, timestamp, extraction method, and privacy label |
| Internal Drive, Gmail, private docs, private repos | Use only connected or explicitly allowed tools | Preserve pointer and role; avoid copying sensitive content into public reports |
| Permission-gated or unavailable material | Do not infer contents | Record access gap and downgrade dependent claims |
| Hypothesis or inference | Do not treat as direct evidence | Link to motivating evidence and keep as candidate until downstream review |

## Gap-To-Action Backflow

When TraceGuard or LogicGuard reports a gap, convert it into SourceGuard search planning:

| Gap | SourceGuard search action |
| --- | --- |
| Missing primary source | primary source search, source-domain search |
| Missing independent source | independent report search, local media, regulator, expert source |
| One-sided support | counterevidence search, limiting evidence search |
| Weak signals only | primary source + independent + counter/limiting search |
| Missing execution or outcome evidence | public record, procurement, operating record, local report, stakeholder, image, video, report-page search |
| Missing date or freshness | exact phrase, dated report, newer source, archive/version check |
| Missing location | map/location search, local source, image search |
| Missing PDF/book page | PDF page or book index/page search |
| Missing image/video/audio anchor | image, reverse image, video segment, transcript, or audio segment search |
| Contradiction | freshness-focused search, original record search, limiting evidence search |
| Permission gap | access gap unless user provides authorized access |

## Search Tactic Catalog

For important leads, choose tactics by evidence role rather than repeating one generic keyword search. Common tactics:

| Tactic | Use when | Guardrail |
| --- | --- | --- |
| `original-source` | A claim needs primary or closest-available records | Do not treat summaries as primary records |
| `specific-site` | The user, source policy, or evidence role points to a known domain, publisher, repository, or archive | Preserve the site/domain searched and access limits |
| `source-lineage` | A claim, rumor, quotation, or statistic needs its origin traced | Do not cite later repeats as origin unless lineage is checked |
| `independent-source` | Support is one-sided, official-only, vendor-only, or otherwise dependent | Record independence limits when sources share origin |
| `counter-limiting` | A claim may be overstated, contested, or scope-limited | Preserve limiting evidence instead of treating it as noise |
| `execution-outcome` | A claim says something happened, launched, operated, changed behavior, or produced impact | Separate announcement evidence from implementation or outcome evidence |
| `freshness` | A current-state or recent-event claim may have changed | Record source date and coverage period |
| `stakeholder` | Affected actors, implementers, critics, users, residents, companies, or regulators may materially change interpretation | Do not make stakeholder quotes stand in for event facts |
| `absence-signal` | The likely record should exist if a claim were established | Record searched sources and coverage before treating non-findings as meaningful |
| `multimodal-anchor` | A claim depends on an image, chart, PDF page, map, video, audio, table, row, or timestamp | Do not invent OCR, transcript, or visual/audio content without extraction input |

## Observation Rules

After a search:

1. Record a `SourceRecord` first. Default status is candidate.
2. Record `EvidenceAnchor` only for specific paragraphs, pages, figures, timestamps, tables, rows, citations, image regions, maps, or segments.
3. Do not invent OCR, transcript, visual recognition, audio content, or inaccessible text.
4. Mark permission-gated or unavailable material as access gap.
5. Record contradictions and limiting evidence instead of overwriting earlier support.
6. Replan after important observations.

For every important source-reading observation, record as much of this support boundary as is known:

```text
what the source says
what it can support
what it cannot support
source role
source date or freshness
coverage period
locator
contradiction or limitation
new lead or follow-up tactic
handoff readiness: SourceGuard only | TraceGuard-ready | LogicGuard-candidate | omit/downgrade
```

Title relevance, snippet relevance, or source existence alone is not enough for promotion. A source that has not been read or anchored remains a candidate.

## Handoff To TraceGuard

Hand off to TraceGuard when there are enough candidate sources and anchors to model event facts, timelines, contradictions, or storylines. Export only sources and anchors. Do not generate validated events in SourceGuard.

TraceGuard may return gaps. Those gaps should feed back into SourceGuard unless the claim is downgraded or the gap is accepted.

## Handoff To LogicGuard

Hand off to LogicGuard only selected material that is stable, important to final claims, and clearly labeled by source role, date/freshness, anchor, limitation, and claim use.

Do not bulk-promote raw search results, duplicate hits, weak signals, or unanchored candidates into LogicGuard.

## Downgrade Rules

Downgrade the report when:

- critical SourceGuard gaps remain open;
- important material is permission-gated or unavailable;
- only weak signals exist;
- counter/limiting search is incomplete for contested claims;
- multimodal material lacks locator or actual extraction input;
- TraceGuard or LogicGuard sends the task back for more source support.

Use ordinary reader-facing wording such as "the available record does not establish", "the evidence is incomplete", or "this remains a working hypothesis".
