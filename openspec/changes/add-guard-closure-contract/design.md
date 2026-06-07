## Overview

Add `research_closure_check.py` to aggregate existing deterministic helper scripts and ledger status into a shared Guard closure report.

## Design

- Existing helpers remain the source of citation/source structural checks.
- The aggregate helper reports missing required ledger fields, stale final artifact status, skipped checks, and next actions.
- Source-related hard errors route back to SourceGuard or claim downgrade.
- Stale final-artifact evidence routes back to FlowGuard freshness handling.

## Risks

- The helper does not replace LogicGuard semantic source-fit judgment.
- It prevents premature closure but cannot prove factual truth by itself.
