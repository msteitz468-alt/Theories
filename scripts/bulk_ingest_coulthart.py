#!/usr/bin/env python3
"""Bulk-create wiki pages for Ross Coulthart — *In Plain Sight* (2021).

Strict-extraction ingest: every page records only what the source asserts.
Coulthart repeatedly flags his own scepticism in the text; where he does, that
qualification is preserved (it is part of what the source says).

Templates are written flush-left (no textwrap.dedent) so that multi-line YAML
blocks substituted into the frontmatter keep valid 2/4-space nesting.
"""
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent / "wiki"
SOURCE = "[[In Plain Sight: An Investigation into UFOs and Impossible Science (Coulthart, 2021)]]"
TOPIC = "ufo-disclosure"
TODAY = "2026-06-07"


def write_page(path: Path, content: str) -> bool:
    """Overwrite-safe writer (all target slugs are unique to this ingest)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")
    return True


def _related(related):
    return "\n".join(f"- [[{r}]]" for r in (related or []))


def claim_page(title, slug, date_or_period, actors, location, contexts,
               prevalence, statement, evidence, contexts_note,
               related, opposing=None):
    actors_yaml = "\n".join(
        f'  - type: {a["type"]}\n    link: "[[{a["link"]}]]"' for a in actors)
    opp = ""
    if opposing:
        opp = f"\n## Opposing Information Within the Source\n\n{opposing}\n"
    return f"""---
title: "{title}"
type: claim
date_or_period: "{date_or_period}"
involved_actors:
{actors_yaml}
location: "{location}"
source_attribution: "{SOURCE}"
contexts: {contexts}
prevalence_in_source: "{prevalence}"
status: extracted
last_updated: {TODAY}
tags: [claim, source/coulthart-2021, topic/{TOPIC}]
---

## Claim Statement

{statement}

## Source Attribution and Direct Evidence

{evidence}

## Contexts Within the Source

{contexts_note}
{opp}
## Related Entities

- {SOURCE}
{_related(related)}
"""


def person_page(title, slug, also, roles, body, related=None, tags=None):
    tags = tags or ["person", f"topic/{TOPIC}"]
    roles_yaml = "\n".join(f"  - {r}" for r in roles)
    also_yaml = ("[" + ", ".join(f'"{a}"' for a in also) + "]") if also else "[]"
    return f"""---
title: "{title}"
type: person
also_known_as: {also_yaml}
roles:
{roles_yaml}
textual_sources:
  - "{SOURCE}"
last_updated: {TODAY}
tags: {tags}
---

{body}

## Related Entities

- {SOURCE}
{_related(related)}
"""


def group_page(title, slug, category, also, body, related=None, tags=None):
    tags = tags or ["group", f"topic/{TOPIC}"]
    also_yaml = ("[" + ", ".join(f'"{a}"' for a in also) + "]") if also else "[]"
    return f"""---
title: "{title}"
type: group
category: {category}
also_known_as: {also_yaml}
periods_active: []
textual_sources:
  - "{SOURCE}"
roles_significance: []
last_updated: {TODAY}
tags: {tags}
---

{body}

## Related Entities

- {SOURCE}
{_related(related)}
"""


def location_page(title, slug, also, body, related=None, tags=None):
    tags = tags or ["location", f"topic/{TOPIC}"]
    also_yaml = ("[" + ", ".join(f'"{a}"' for a in also) + "]") if also else "[]"
    return f"""---
title: "{title}"
type: location
also_known_as: {also_yaml}
periods_inhabited: []
modern_geography: []
associated_peoples: []
last_updated: {TODAY}
tags: {tags}
---

{body}

## Related Entities

- {SOURCE}
{_related(related)}
"""


def event_page(title, slug, date_start, date_end, participants, location,
               overview, key_claims=None, related=None, tags=None):
    tags = tags or ["event", f"topic/{TOPIC}"]
    parts = "\n".join(f'  - "[[{p}]]"' for p in participants) or "  []"
    kc = ("[" + ", ".join(f'"[[{c}]]"' for c in key_claims) + "]") if key_claims else "[]"
    return f"""---
title: "{title}"
type: event
date_start: "{date_start}"
date_end: "{date_end}"
participants:
{parts}
location: "{location}"
key_claims: {kc}
sources_ingested: 1
last_updated: {TODAY}
tags: {tags}
---

## Event Overview

{overview}

## Related Entities

- {SOURCE}
{_related(related)}
"""


def concept_page(title, slug, also, body, related=None, tags=None):
    tags = tags or ["concept", f"topic/{TOPIC}"]
    also_yaml = ("[" + ", ".join(f'"{a}"' for a in also) + "]") if also else "[]"
    return f"""---
title: "{title}"
type: concept
also_known_as: {also_yaml}
last_updated: {TODAY}
tags: {tags}
---

{body}

## Related Entities

- {SOURCE}
{_related(related)}
"""


def controversy_page(title, slug, locus, positions, body, related=None, tags=None):
    tags = tags or ["controversy", f"topic/{TOPIC}"]
    pos = "\n".join(f'  - "{p}"' for p in positions)
    return f"""---
title: "{title}"
type: controversy
text_locus: "{locus}"
positions_presented:
{pos}
last_updated: {TODAY}
tags: {tags}
---

{body}

## Related Entities

- {SOURCE}
{_related(related)}
"""


if __name__ == "__main__":
    import ingest_coulthart_data as data
    # expose write_page under the name the data module's run() expects
    g = dict(globals())
    g["write_if_new"] = write_page
    data.run(g)
