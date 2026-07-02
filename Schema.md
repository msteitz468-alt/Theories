# Historical Claims LLM Wiki Schema

**Modeled directly on the structure and detail level of the Religious Commentary Wiki schema (CLAUDE.md), adapted for compiling historical claims, groups, events, persons, sources, locations, and related entities.**

This is a persistent, LLM-maintained Obsidian wiki for the structured cataloging of historical claims and their supporting contexts. The wiki focuses on atomic, attributable claims drawn from source material, organized through dedicated pages for events, groups, persons, sources, locations, periods, and concepts.

**Core principle (strict extraction)**: When you provide source material, the LLM extracts and structures **only** what is explicitly present in that source. It does not add external counter-commentary, modern historiography, or training-data rebuttals unless they appear in the provided source. Default behavior is faithful extraction and organization.

You (the human) source documents and direct focus. The LLM handles all writing, cross-referencing, filing, and maintenance of the `wiki/` directory.

The working environment is Obsidian. All files are Markdown. Raw source material lives in `raw-sources/`. The wiki lives in `wiki/`. Never modify files in `raw-sources/`.

**Filing raw sources**: When a source is ingested, its raw file must be placed in `raw-sources/texts/` (create the subfolder if it does not yet exist). Do not leave ingested source files loose in the `raw-sources/` root. Supporting scholarship and image assets go in `raw-sources/scholarship/` and `raw-sources/assets/` respectively.

---

## Directory Structure

```
raw-sources/                     # Immutable source documents (PDFs, text files, images, etc.)
    texts/                       # Primary historical texts, documents, inscriptions
    scholarship/                 # Modern academic works, articles, books
    assets/                      # Maps, photos, diagrams, manuscript images

wiki/                            # LLM-maintained knowledge base
    claims/                      # Atomic historical claims (the core unit)
        {topic}/                 # Topic subfolders — one per subject area (see below)
    events/                      # Specific historical occurrences with time, place, participants
        {topic}/                 # Topic subfolders — same topic names as claims/
    groups/                      # Peoples, tribes, nations, polities, religious parties, movements, collectives
    persons/                     # Historical individuals (rulers, generals, thinkers, etc.)
    sources/                     # Detailed pages on primary and secondary sources used
    locations/                   # Geographical places with historical context and modern identification
    phenomena/                   # Competing explanations of major physical monuments or historical mysteries
    periods/                     # Eras, ages, reigns, and chronological frameworks
    concepts/                    # Key historical, political, social, or historiographical concepts
    controversies/               # Disputed interpretations, conflicting accounts, or contested claims
        {topic}/                 # Topic subfolders — same topic names as claims/
    comparisons/                 # Cross-source or cross-period comparison pages (filed when useful)
    queries/                     # Filed answers to significant questions (when synthesis is non-trivial)

scripts/                         # Python linting and maintenance tools (validate_schema.py, etc.)
```

**No master `index.md` or `log.md`** is maintained automatically. The LLM does not create or update a central index or append-only log on every ingest unless you explicitly request it for a specific session.

---

## Page Types and Formats

### Claim Topics (`wiki/claims/{topic}/`)

Claims are organised into topic subfolders. Each topic is a kebab-case directory name, e.g. `area-51/`, `holy-grail/`, `cold-war/`. **New topics are created on demand** — when a new source introduces claims that don't fit any existing topic, create a new subfolder with a short descriptive name and file the claims there. There is no registry of valid topics; any subfolder inside `claims/` is a valid topic.

**Current topics (as of last reorganisation):**

| Folder | Contents |
|--------|----------|
| `area-51/` | Area 51 base secrecy, governance, access control |
| `cold-war/` | U-2/Oxcart programs, CIA covert ops, MiGs, drone programs |
| `nuclear/` | Atomic tests, accidents, nuclear secrecy |
| `ufo-disclosure/` | Roswell, Bob Lazar, S-4, UFO cover-up claims |
| `holy-grail/` | Holy Blood / Holy Grail thesis, Prieuré de Sion, Merovingians, Saunière |
| `illuminati-reptilian/` | Icke's reptilian bloodline, Illuminati, and Anunnaki claims |
| `nwo-conspiracy/` | Cooper's elite New World Order and consciousness claims |
| `reality-transurfing/` | Zeland's Transurfing model: alternatives space, pendulums, intention, slides, outer intention |
| `federal-reserve/` | Mullins's and Griffin's accounts of the Federal Reserve's secret origins, ownership, war finance, engineered depressions, and London/Hitler connections |
| `round-table-cfr/` | Quigley's account of the Rhodes-Milner Round Table secret society and its evolution into the RIIA and Council on Foreign Relations |
| `wall-street-bolshevik/` | Sutton's documentary account of Wall Street (Guaranty Trust / 120 Broadway) financing of the Bolshevik Revolution |
| `ancient-astronauts/` | Sitchin's *Twelfth Planet*: the Nefilim/Anunnaki as astronauts from planet Nibiru, the Enuma Elish as cosmogony, genetic creation of man, and the Deluge |

When linking to a claim from another page, use the standard `[[Claim Title]]` wikilink — Obsidian resolves titles regardless of subfolder, so paths do not need to be specified in links.

---

### Claim Page (`wiki/claims/{topic}/`)
The fundamental atomic unit. Every substantive assertion that can be isolated from a source should become (or link to) a claim page.

```yaml
---
title: [Short, precise claim title — e.g. "Hannibal crossed the Alps in 218 BC via the Col de la Traversette"]
type: claim
date_or_period: [e.g. "218 BC", "c. 218–201 BC (Second Punic War)", "reign of Augustus (27 BC–14 AD)"]
involved_actors:
  - type: person
    link: "[[Scipio Africanus (236–183 BC)]]"
  - type: group
    link: "[[Carthage (Punic period)]]"
location: "[[Col de la Traversette]] or text description"
source_attribution: "[[Polybius Histories Book 3]] and [[Livy Ab Urbe Condita Book 21]]"
contexts: [e.g. "Polybius' narrative of the Second Punic War", "Livy's moralizing account"]
prevalence_in_source: [e.g. "central claim in Polybius", "mentioned in passing in Livy"]
status: draft | extracted | expanded | needs-review
last_updated: [YYYY-MM-DD]
tags: [claim, period/punic-wars, source-type/literary]
---
```

**Body structure**:

**Claim Statement**  
Precise restatement of what the source asserts.

**Source Attribution and Direct Evidence**  
Exact references, quotes, or paraphrases from the provided source that support the claim. Include chapter/verse or section numbers where available.

**Contexts Within the Source**  
How the source frames or qualifies the claim (author's perspective, narrative purpose, any caveats the source itself makes).

**Opposing Information Within the Source** (only if present)  
If the source itself presents contradictory data, alternative accounts, or internal tensions regarding this claim, record them here with direct references. Do not import external counter-arguments.

**Related Entities**  
Links to relevant event, group, person, location, or source pages created or updated from the same source material.

---

### Event Topics (`wiki/events/{topic}/`)

Events are organised into topic subfolders using the same topic names as `claims/`. **New topics are created on demand.** Current topics mirror those in `claims/` (e.g. `area-51/`, `cold-war/`, `nuclear/`, `ufo-disclosure/`, `holy-grail/`). Wikilinks use `[[Event Title]]` format — Obsidian resolves by title regardless of subfolder.

**Title prefix convention**: Event page titles begin with `"Event: "` when the linked source corpus uses that prefix in cross-references (primarily the Holy Grail / medieval history cluster). Area 51 and Cold War event pages do not use the prefix; their titles are plain descriptive strings.

---

### Controversy Topics (`wiki/controversies/{topic}/`)

Controversies are organised into topic subfolders using the same topic names as `claims/`. Current topics: `area-51/`, `holy-grail/`. Wikilinks use `[[Controversy Title]]` format.

---

### Event Page (`wiki/events/{topic}/`)
For specific, bounded historical occurrences.

```yaml
---
title: [Event Name with date disambiguation — e.g. "Battle of Cannae (216 BC)"]
type: event
date_start: [approximate or exact]
date_end: [approximate or exact]
participants:
  - "[[Roman Republic (3rd century BC)]]"
  - "[[Carthage (Punic period)]]"
  - "[[Hannibal Barca (247–183 BC)]]"
location: "[[Cannae]]"
key_claims: ["[[Claim: Roman losses at Cannae exceeded 50,000]]", ...]
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [event, period/punic-wars]
---
```

**Body structure**:

**Event Overview** (drawn only from provided sources)  
Narrative summary of what happened according to the source(s) being ingested.

**Participants and Their Roles**  
How the source describes the actors involved.

**Key Claims Arising from This Event**  
Links to atomic claim pages extracted from the source material about this event.

**Source-Specific Portraits**  
If multiple sources are being processed together, note differences in how they portray the event (only differences present in the provided material).

**Related Entities**  
Links to group, person, location, and claim pages.

---

### Group Page (`wiki/groups/`)
For peoples, tribes, nations, polities, religious parties, movements, and other collectives treated as actors in historical sources.

```yaml
---
title: [Group Name with period disambiguation — e.g. "Carthage (Punic period)"]
type: group
category: polity | ethnic_group | tribal_confederation | religious_party | military_alliance | ideological_movement
also_known_as: [self-designations, exonyms, variants]
periods_active: [e.g. "c. 814 BC – 146 BC"]
textual_sources: []   # primary sources where the group appears as actor
roles_significance: []  # e.g. commercial power, military rival, subject of Roman moralizing
last_updated: [YYYY-MM-DD]
tags: [group, period/ancient, category/polity]
---
```

**Body structure**:

**Identity and Nomenclature** (from the source)  
How the source names the group, any self-designations mentioned, and outsider labels used in the text.

**Primary Textual Appearances**  
Key passages in the provided source(s) where the group acts or is described. One-line summaries of what each contributes to the portrait.

**Source-Specific Portraits**  
How the current source(s) portray the group's character, institutions, territory, leadership, and relations with others. Stay within the provided material.

**Related Claims and Events**  
Links to atomic claims and events involving this group extracted from the current source(s).

**Related Entities**  
Links to person, location, and concept pages created or updated from the same material.

---

### Person Page (`wiki/persons/`)
For historical individuals who appear as significant actors.

```yaml
---
title: [Person Name with dates — e.g. "Hannibal Barca (247–183 BC)"]
type: person
also_known_as: [titles, epithets]
roles: [e.g. general, statesman, suffet]
textual_sources: []   # primary sources where the person is prominent
last_updated: [YYYY-MM-DD]
tags: [person, period/punic-wars]
---
```

**Body structure**:

**Biographical Details from Source**  
What the provided source(s) say about the person's life, actions, and characteristics. Distinguish textual claims from any historical-critical notes only if the source itself does so.

**Primary Source Appearances**  
Key passages and what they contribute to the portrait.

**Related Claims, Events, and Groups**  
Links generated from the current source material.

---

### Source Page (`wiki/sources/`)
For detailed treatment of a primary or secondary source being ingested.

```yaml
---
title: [Source Title or Standard Abbreviation]
type: source
source_type: primary_literary | primary_epigraphic | primary_archaeological | secondary_scholarly | etc.
source_category: primary_experience | primary_revelatory | secondary_synthesis | primary_document
author_or_origin: []
date_composed: []
language_original: []
last_updated: [YYYY-MM-DD]
tags: [source, type/primary-literary]
---
```

**Body structure**:

**Source Description** (from the material itself or standard identification in the provided text)  
Author, date, genre, scope as presented in the source or the current document.

**What the Source Contributes**  
Summary of the claims, events, groups, persons, and locations it supplies in the current ingest.

**Chapter Summaries** (for sources ingested chapter-by-chapter)  
A section-by-section walkthrough of the source, following its own divisions (prologue, numbered chapters, parts, appendices, epilogue). Adjacent chapters with little individual material may be grouped under a combined heading (e.g. `### Chapters 4–8: ...`). Each chapter heading is followed by:

- A prose summary of what that chapter presents, staying strictly within the source (specific figures, named participants, and key episodes are welcome, but no external commentary).
- **Claims Extracted** — `[[wikilinks]]` to the atomic claim pages drawn from that chapter. The same claim may legitimately recur under several chapters.
- **Persons**, **Groups**, **Locations**, **Events** — optional bolded sub-lists of `[[wikilinks]]` to the relevant entity pages introduced or developed in that chapter. Include only the categories that actually appear.

Omit this section entirely for sources that were not ingested at chapter granularity. The aggregate **Key Claims Extracted** list below still collects every claim from the source in one place.

**Key Claims Extracted**  
Links to claim pages created from this source. For chapter-ingested sources this is the de-duplicated union of the per-chapter **Claims Extracted** lists.

**Internal Tensions or Multiple Accounts** (only if present in the source)  
Record any places where the source itself presents conflicting information or alternative traditions.

---

### Phenomenon Page (`wiki/phenomena/`)
For physical structures, monuments, or historical mysteries that have competing explanations across multiple sources.

```yaml
---
title: [Phenomenon Name — e.g. "Great Pyramid of Giza"]
type: phenomenon
locations:
  - "[[Giza Plateau]]"
associated_claims:
  - "[[Claim: Outer Intention Was Used to Build the Egyptian Pyramids]]"
last_updated: [YYYY-MM-DD]
tags: [phenomenon, region/egypt]
---
```

**Body structure**:

**Phenomenon Overview** (neutral physical description)  
Brief, sourced description of what the object or mystery is physically.

**Competing Source-Specific Explanations**  
A list of how each source explains the phenomenon's construction or purpose:
- **Source A** (e.g. Sitchin): Summary of explanation with links to key claims.
- **Source B** (e.g. Zeland): Summary of explanation with links to key claims.

**Related Entities**  
Links to location, group, person, and claim pages.

---

### Location Page (`wiki/locations/`)
For places with narrative, strategic, or identificatory weight in the sources.

```yaml
---
title: [Location Name with modern identification — e.g. "Cannae (near modern Canosa di Puglia)"]
type: location
also_known_as: [ancient variants, modern names]
periods_inhabited: [summary from source or archaeological notes in the provided material]
modern_geography: [current identification, coordinates if given in source]
associated_peoples: []  # groups mentioned in connection with the site in the source
last_updated: [YYYY-MM-DD]
tags: [location, period/ancient]
---
```

**Body structure**:

**Geographical and Historical Context from Source**  
Physical setting and historical notes present in the provided material.

**Textual Appearances**  
How the location features in the source(s) — as setting for events, as territory of a group, etc.

**Related Claims and Events**  
Links to claims and events tied to this location in the current source material.

---

### Period / Concept Page (`wiki/periods/` and `wiki/concepts/`)
Use for chronological frameworks or recurring analytical categories when they receive sustained treatment in sources.

YAML and body structure follow similar patterns: definition/characterization from the source, key claims or events associated with the period/concept in the current material, and cross-links.

**Title prefix convention**: Concept page titles begin with `"Concept: "` when the source corpus uses that prefix in cross-references (primarily the Holy Grail / Cooper clusters). Plain descriptive titles (e.g. `"Black operations (US government)"`) are used for concepts that are linked to without the prefix.

---

### Controversy Page (`wiki/controversies/`)
Only create when the provided source itself highlights a dispute, conflicting accounts, or contested interpretation.

```yaml
---
title: [Nature of the dispute — e.g. "Conflicting accounts of Roman casualties at Cannae"]
type: controversy
text_locus: [specific passage or event in the source]
positions_presented: []  # list the different accounts given in the source
last_updated: [YYYY-MM-DD]
tags: [controversy]
---
```

---

## Ingest Workflow (Strict Extraction)

When you provide a new source:

1. **Identify** the source type and scope.
2. **Extract** atomic claims, events, groups, persons, locations, and concepts that appear with sufficient substance in the provided material.
3. **Create or update** the relevant pages in `wiki/`:
   - Write or update claim pages for every isolatable assertion.
   - Create or update event, group, person, location, source, period, and concept pages as warranted by the material.
   - Only populate `evidence_against` or controversy elements if the source itself contains them.
4. **Cross-link** the new or updated pages using precise `[[Exact Title]]` wikilinks.
5. **Stay strictly within the source**. Do not add external commentary, dates, identifications, or counter-claims not present in the material you provided.

A single source may legitimately touch 5–15 wiki pages. This is normal.

---

## Contradiction / Multiple Perspectives Protocol

When the source(s) you provide contain internal contradictions or present multiple accounts:

- Record each position or account separately on the relevant claim or controversy page.
- Attribute each clearly to its source or section within the provided material.
- Do **not** adjudicate which account is more accurate.
- Do **not** import external scholarly resolutions unless they appear in the source you gave.

If you want the LLM to compare the current source against previously ingested material or external knowledge, you must explicitly request "balanced mode" or "compare with existing wiki content."

---

## Query Workflow

When you ask a question about the wiki:

1. Identify relevant pages from the folder structure and existing links.
2. Read the relevant pages.
3. Synthesize an answer using only the content of those pages (or the specific sources being discussed).
4. If the answer involves non-trivial synthesis across multiple pages, offer to file it as a `wiki/queries/` page.
5. Do not add external information.

---

## Maintenance and Lint Workflow

### Python environment

The lint scripts depend on the third-party package `PyYAML`. A dedicated virtual
environment lives at the repo root in **`.venv/`**. Always run the scripts with
that interpreter so the dependency resolves:

```bash
# from the repo root (/home/mark/Documents/Theories)
.venv/bin/python scripts/validate_schema.py
.venv/bin/python scripts/lint_all.py
```

`lint_all.py` invokes the other scripts via `sys.executable`, so launching it
through `.venv/bin/python` propagates the venv to the whole suite.

To (re)create the environment after a fresh clone or a wipe of `.venv/`:

```bash
python3 -m venv .venv
.venv/bin/pip install -r scripts/requirements.txt
```

Pinned dependencies are listed in `scripts/requirements.txt`. The `.venv/`
directory is excluded from all tree-walking scripts via their `SKIP_PARTS` set,
so it is never scanned as wiki content.

### Scripts

Run the Python scripts in `scripts/` periodically (especially after batches of ingests):

- `validate_schema.py` — checks required fields, valid status values, etc.
- `check_wikilinks.py` — reports broken wikilinks.
- `review_queue.py` — lists claims or pages with `status: needs-review` or low extraction completeness.
- `lint_all.py` — runs the full suite and writes reports to `wiki/` if configured.

Manual lint checks the LLM can perform when asked:
- Pages (especially claims) with very thin `evidence_for` sections.
- Groups, persons, or locations mentioned repeatedly in claims/events but lacking their own dedicated pages.
- Claims that appear in multiple sources but have not been cross-linked.
- Potential duplicate claims (similar wording across different sources).

---

## Naming and Linking Conventions

- File names: `kebab-case.md` with clear disambiguation (e.g. `battle-of-cannae-216-bc.md`, `hannibal-barca-247-183-bc.md`, `carthage-punic-period.md`).
- All internal links use Obsidian `[[Exact Title]]` format.
- Use consistent disambiguation in titles so links are unambiguous.
- Transliteration: Follow standard academic conventions for the relevant languages (SBL for Hebrew, standard for Greek/Latin, etc.). Document any project-specific choices in a `wiki/concepts/transliteration.md` page if needed.

---

## Division of Labor

**You (human)**: Source documents, decide what to ingest and what questions to ask, review and accept/reject proposed edits, run lint scripts when desired, and maintain overall direction.

**LLM**: All writing and updating of files inside `wiki/`. All cross-referencing. All structuring of extracted material into the defined page types. All proposals for new or changed pages must be output in full, ready-to-paste Markdown format.

---

## Scope

For a list of ingested sources, see [[wiki/sources/INDEX.md]]. Do not maintain a source inventory here.

---

This schema gives you the detailed, type-specific structure and workflow discipline of the religious commentary model while staying tightly aligned with your goal of **source-faithful extraction and cataloging of historical claims** (including groups, events, etc.) without unwanted external counter-commentary. 

The Python linting scripts from the previous version remain compatible and should be kept in `scripts/`.

Copy this file into your `wiki/` folder (or root) as your primary instructions document and point your AI agent to it (or to a short `AGENTS.md` that points here). Let me know if you want any sections expanded, particular page types added, or example pages generated for a test source.