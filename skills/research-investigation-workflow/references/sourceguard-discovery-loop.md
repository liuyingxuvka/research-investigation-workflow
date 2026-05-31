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

## Observation Rules

After a search:

1. Record a `SourceRecord` first. Default status is candidate.
2. Record `EvidenceAnchor` only for specific paragraphs, pages, figures, timestamps, tables, rows, citations, image regions, maps, or segments.
3. Do not invent OCR, transcript, visual recognition, audio content, or inaccessible text.
4. Mark permission-gated or unavailable material as access gap.
5. Record contradictions and limiting evidence instead of overwriting earlier support.
6. Replan after important observations.

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
