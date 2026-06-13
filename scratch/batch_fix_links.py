#!/usr/bin/env python3
"""
batch_fix_links.py
===================
Phase 1: Add missing aliases to existing notes so broken wikilinks resolve.
Phase 2: Create stub pages for completely missing entities.

Run from the repo root:
    .venv/bin/python scratch/batch_fix_links.py
"""

import re
import sys
from pathlib import Path

WIKI = Path("wiki")

# ─────────────────────────────────────────────────────────────────────────────
# PHASE 1 — Add aliases to existing files
# ─────────────────────────────────────────────────────────────────────────────

# Each entry: (relative path from repo root, field_to_use, new_aliases_to_add)
# field_to_use is either "also_known_as" or "aliases"
ALIAS_ADDITIONS = [
    # concepts
    ("wiki/concepts/Vibrational_State.md",          "aliases",      ["Vibrational State"]),
    ("wiki/concepts/alternatives-space.md",          "also_known_as", ["alternatives-space"]),
    ("wiki/concepts/halls-of-amenti.md",             "also_known_as", ["halls-of-amenti"]),
    ("wiki/concepts/hemisync.md",                    "also_known_as", ["hemisync"]),
    ("wiki/concepts/holographic-brain-model.md",     "also_known_as", ["holographic-brain-model"]),
    ("wiki/concepts/implicate-and-explicate-order.md","also_known_as", ["implicate-and-explicate-order"]),
    ("wiki/concepts/i-there-cluster.md",             "also_known_as", ["i-there-cluster"]),
    ("wiki/concepts/well-being-stream.md",           "also_known_as", ["well-being-stream"]),
    ("wiki/concepts/focus-levels-monroe-locales.md", "also_known_as", ["Focus Levels (Monroe)", "Focus Levels Map"]),
    ("wiki/concepts/Locales_in_Non-Physical_Reality.md", "aliases",  ["Locales in Non-Physical Reality"]),
    ("wiki/concepts/The_Separation_Process.md",      "aliases",      ["The Separation Process"]),
    ("wiki/concepts/TBC_The_Big_Computer.md",        "aliases",      ["TBC (The Big Computer)"]),
    ("wiki/concepts/Psi_Uncertainty_Principle.md",   "aliases",      ["The Psi Uncertainty Principle"]),
    # sources
    ("wiki/sources/Campbell_My_Big_TOE.md",          "also_known_as", ["My Big TOE"]),
    ("wiki/sources/far-journeys-monroe-1985.md",     "also_known_as", ["Far Journeys"]),
    ("wiki/sources/ultimate-journey-monroe-1994.md", "also_known_as", ["Ultimate Journey"]),
    ("wiki/sources/coleman-conspirators-hierarchy-committee-of-300-1992.md", "also_known_as",
        ["Conspirators' Hierarchy: The Story of the Committee of 300 (John Coleman, 1992)"]),
    ("wiki/sources/allen-abraham-none-dare-call-it-conspiracy-1971.md", "also_known_as",
        ["None Dare Call It Conspiracy (Gary Allen, Larry Abraham)"]),
    ("wiki/sources/the-club-of-rome-coleman-2008.md", "also_known_as",
        ["The Club of Rome (John Coleman, 2008)"]),
    ("wiki/sources/hoffman-case-against-reality-2019.md", "also_known_as",
        ["The Case Against Reality: Why Evolution Hid the Truth from Our Eyes (Hoffman)"]),
    ("wiki/sources/the-essential-law-of-attraction-collection-hicks-2013.md", "also_known_as",
        ["The Essential Law of Attraction Collection (Hicks)"]),
    ("wiki/sources/roberts-personal-reality-1974.md", "also_known_as",
        ["The Nature of Personal Reality (Roberts, 1972)"]),
    ("wiki/sources/roberts-seth-speaks-1972.md",     "also_known_as",
        ["Seth Speaks: The Eternal Validity of the Soul (Roberts, 1972)"]),
    # persons
    ("wiki/persons/Thomas_Campbell_physicist.md",    "also_known_as", ["Thomas Campbell"]),
    ("wiki/persons/Jane_Roberts_Seth.md",            "also_known_as", ["Jane Roberts"]),
    # groups
    ("wiki/groups/council-on-foreign-relations.md",  "also_known_as", ["Council on Foreign Relations (Cooper)"]),
    ("wiki/groups/skull-and-bones.md",               "also_known_as", ["Skull and Bones (Cooper)"]),
    ("wiki/groups/project-blue-book-us-air-force.md","also_known_as",
        ["Project SIGN / GRUDGE / Blue Book (Cooper)"]),
    # claims (add short alias to long existing titles)
    ("wiki/claims/consciousness-obe/consciousness-ratio-subjective-objective-time.md", "also_known_as",
        ["Consciousness is defined by subjective time dilation relative to objective clock time"]),
]


def _get_frontmatter_block(text: str):
    """Return (yaml_text, body_text) or None if no frontmatter."""
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    yaml_text = text[3:end]
    body_text = text[end + 4:]
    return yaml_text, body_text


def add_aliases_to_file(filepath: str, field: str, new_aliases: list[str]):
    p = Path(filepath)
    if not p.exists():
        print(f"  [SKIP] Not found: {filepath}")
        return

    text = p.read_text(encoding="utf-8")
    result = _get_frontmatter_block(text)
    if result is None:
        print(f"  [SKIP] No frontmatter: {filepath}")
        return

    yaml_text, body = result

    # Check if field already exists
    field_pattern = re.compile(rf"^{re.escape(field)}\s*:", re.MULTILINE)
    match = field_pattern.search(yaml_text)

    if match:
        # Field exists — find its value and append new aliases
        # Detect whether it's a scalar, inline list, or block list
        after_field = yaml_text[match.end():]

        # Inline list: also_known_as: [a, b, c]
        inline_match = re.match(r'\s*\[([^\]]*)\]', after_field)
        if inline_match:
            existing_raw = inline_match.group(1)
            # Parse existing entries
            existing = [e.strip().strip('"\'') for e in existing_raw.split(',') if e.strip()]
            to_add = [a for a in new_aliases if a not in existing]
            if not to_add:
                print(f"  [OK]  Already has aliases {new_aliases}: {filepath}")
                return
            new_list_str = ', '.join(
                [f'"{e}"' for e in existing] + [f'"{a}"' for a in to_add]
            )
            new_yaml = yaml_text[:match.end()] + f' [{new_list_str}]' + after_field[inline_match.end():]
            new_text = f"---{new_yaml}\n---{body}"
            p.write_text(new_text, encoding="utf-8")
            print(f"  [UPDATED inline] Added {to_add} → {filepath}")
            return

        # Scalar: also_known_as: SomeName
        scalar_match = re.match(r'\s+(\S[^\n]*)', after_field)
        block_list_match = re.match(r'\n', after_field)

        # Block list: also_known_as:\n  - a\n  - b
        block_match = re.match(r'\s*\n((?:\s*-\s*.+\n?)+)', after_field)
        if block_match:
            existing_items_text = block_match.group(1)
            existing = [re.sub(r'^\s*-\s*', '', l).strip().strip('"\'')
                        for l in existing_items_text.splitlines() if l.strip()]
            to_add = [a for a in new_aliases if a not in existing]
            if not to_add:
                print(f"  [OK]  Already has aliases {new_aliases}: {filepath}")
                return
            append_lines = ''.join(f'  - "{a}"\n' for a in to_add)
            insert_pos = match.end() + block_match.end()
            new_yaml = yaml_text[:insert_pos] + append_lines + yaml_text[insert_pos:]
            new_text = f"---{new_yaml}\n---{body}"
            p.write_text(new_text, encoding="utf-8")
            print(f"  [UPDATED block] Added {to_add} → {filepath}")
            return

        # Scalar or empty value: replace with list
        if scalar_match:
            existing_val = scalar_match.group(1).strip().strip('"\'')
            all_aliases = [existing_val] + [a for a in new_aliases if a != existing_val]
        else:
            all_aliases = new_aliases

        new_list_str = ', '.join(f'"{a}"' for a in all_aliases)
        new_yaml = yaml_text[:match.end()] + f' [{new_list_str}]\n' + after_field.lstrip('\n').lstrip(' ').lstrip(scalar_match.group(0) if scalar_match else '')
        # Simpler: just replace the matched line
        # Rebuild with a block list instead
        block_lines = ''.join(f'\n  - "{a}"' for a in all_aliases)
        # Find end of the existing value line
        line_end = after_field.find('\n')
        if line_end == -1:
            line_end = len(after_field)
        new_yaml = yaml_text[:match.end()] + block_lines + '\n' + yaml_text[match.end() + line_end + 1:]
        new_text = f"---{new_yaml}\n---{body}"
        p.write_text(new_text, encoding="utf-8")
        print(f"  [UPDATED scalar→block] Added {new_aliases} → {filepath}")
        return
    else:
        # Field does not exist — add it before closing ---
        block_lines = ''.join(f'  - "{a}"\n' for a in new_aliases)
        new_field_text = f'{field}:\n{block_lines}'
        # Insert at end of yaml_text
        new_yaml = yaml_text.rstrip('\n') + '\n' + new_field_text
        new_text = f"---{new_yaml}---{body}"
        p.write_text(new_text, encoding="utf-8")
        print(f"  [ADDED field] {field} {new_aliases} → {filepath}")


# ─────────────────────────────────────────────────────────────────────────────
# PHASE 2 — Create stub pages
# ─────────────────────────────────────────────────────────────────────────────

def make_person_stub(path: str, title: str, also_known_as: list[str],
                     roles: list[str], source: str, extra_body: str = ""):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.exists():
        print(f"  [EXISTS] {path}")
        return
    aka_yaml = ""
    if also_known_as:
        lines = "\n".join(f'  - "{a}"' for a in also_known_as)
        aka_yaml = f"also_known_as:\n{lines}\n"
    roles_yaml = "\n".join(f'  - {r}' for r in roles) if roles else "  - historical figure"
    content = f"""---
title: "{title}"
type: person
{aka_yaml}roles:
{roles_yaml}
textual_sources:
  - "{source}"
last_updated: 2026-06-13
tags: [person, stub]
---

## Biographical Details from Source

*Stub — extracted from source material. To be expanded when source is ingested.*
{extra_body}
"""
    p.write_text(content, encoding="utf-8")
    print(f"  [CREATED person] {path}")


def make_group_stub(path: str, title: str, also_known_as: list[str],
                    category: str, source: str, extra_body: str = ""):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.exists():
        print(f"  [EXISTS] {path}")
        return
    aka_yaml = ""
    if also_known_as:
        lines = "\n".join(f'  - "{a}"' for a in also_known_as)
        aka_yaml = f"also_known_as:\n{lines}\n"
    content = f"""---
title: "{title}"
type: group
category: {category}
{aka_yaml}textual_sources:
  - "{source}"
last_updated: 2026-06-13
tags: [group, stub]
---

## Overview from Source

*Stub — extracted from source material. To be expanded when source is ingested.*
{extra_body}
"""
    p.write_text(content, encoding="utf-8")
    print(f"  [CREATED group] {path}")


def make_location_stub(path: str, title: str, also_known_as: list[str],
                       source: str, extra_body: str = ""):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.exists():
        print(f"  [EXISTS] {path}")
        return
    aka_yaml = ""
    if also_known_as:
        lines = "\n".join(f'  - "{a}"' for a in also_known_as)
        aka_yaml = f"also_known_as:\n{lines}\n"
    content = f"""---
title: "{title}"
type: location
{aka_yaml}textual_sources:
  - "{source}"
last_updated: 2026-06-13
tags: [location, stub]
---

## Overview from Source

*Stub — extracted from source material. To be expanded when source is ingested.*
{extra_body}
"""
    p.write_text(content, encoding="utf-8")
    print(f"  [CREATED location] {path}")


def make_event_stub(path: str, title: str, also_known_as: list[str],
                    date: str, source: str, extra_body: str = ""):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.exists():
        print(f"  [EXISTS] {path}")
        return
    aka_yaml = ""
    if also_known_as:
        lines = "\n".join(f'  - "{a}"' for a in also_known_as)
        aka_yaml = f"also_known_as:\n{lines}\n"
    content = f"""---
title: "{title}"
type: event
date_or_period: "{date}"
{aka_yaml}textual_sources:
  - "{source}"
last_updated: 2026-06-13
tags: [event, stub]
---

## Overview from Source

*Stub — extracted from source material. To be expanded when source is ingested.*
{extra_body}
"""
    p.write_text(content, encoding="utf-8")
    print(f"  [CREATED event] {path}")


def make_concept_stub(path: str, title: str, also_known_as: list[str],
                      source: str, extra_body: str = ""):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.exists():
        print(f"  [EXISTS] {path}")
        return
    aka_yaml = ""
    if also_known_as:
        lines = "\n".join(f'  - "{a}"' for a in also_known_as)
        aka_yaml = f"also_known_as:\n{lines}\n"
    content = f"""---
title: "{title}"
type: concept
{aka_yaml}source_attribution: "{source}"
last_updated: 2026-06-13
tags: [concept, stub]
---

## Definition from Source

*Stub — extracted from source material. To be expanded when source is ingested.*
{extra_body}
"""
    p.write_text(content, encoding="utf-8")
    print(f"  [CREATED concept] {path}")


def make_claim_stub(path: str, title: str, also_known_as: list[str],
                    source: str, extra_body: str = ""):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.exists():
        print(f"  [EXISTS] {path}")
        return
    aka_yaml = ""
    if also_known_as:
        lines = "\n".join(f'  - "{a}"' for a in also_known_as)
        aka_yaml = f"also_known_as:\n{lines}\n"
    content = f"""---
title: "{title}"
type: claim
{aka_yaml}source_attribution: "{source}"
last_updated: 2026-06-13
tags: [claim, stub]
---

## Claim Summary

*Stub — extracted from source material. To be expanded when source is ingested.*
{extra_body}
"""
    p.write_text(content, encoding="utf-8")
    print(f"  [CREATED claim] {path}")


# ─────────────────────────────────────────────────────────────────────────────
# STUB DEFINITIONS
# ─────────────────────────────────────────────────────────────────────────────

HOLY_BLOOD_SOURCE = "[[Holy Blood, Holy Grail (Baigent, Leigh & Lincoln)]]"
COOPER_SOURCE = "[[Behold a Pale Horse (Cooper)]]"
CAMPBELL_SOURCE = "[[My Big TOE (A Trilogy Unifying Philosophy, Physics and Metaphysics)]]"
MONROE_JOOB_SOURCE = "[[Journeys Out of the Body (Monroe, 1971)]]"
ELIZONDO_SOURCE = "[[Imminent (Elizondo)]]"
ICKE_SOURCE = "[[The Biggest Secret (Icke)]]"
WALLIS_SOURCE = "[[Escaping from Eden (Wallis)]]"
JACOBS_SOURCE = "[[Area 51 — An Uncensored History of America's Top Secret Military Base (Jacobsen 2010)]]"
VALLEE_SOURCE = "[[Messengers of Deception (Vallee)]]"
ALLEN_SOURCE = "[[None Dare Call It Conspiracy (Allen & Abraham, 1971)]]"
COLEMAN_SOURCE = "[[Conspirators' Hierarchy: The Story of the Committee of 300 (Coleman)]]"
BENTOV_SOURCE = "[[Stalking the Wild Pendulum (Bentov, 1977)]]"
VIRK_SOURCE = "[[The Simulation Hypothesis (Virk)]]"

PERSON_STUBS = [
    # Holy Blood Holy Grail persons
    ("wiki/persons/arnaud-amaury.md",
     "Arnaud-Amaury (Abbot of Cîteaux, papal legate)",
     ["Arnaud-Amaury (papal legate, Abbot of Cîteaux)"],
     ["Cistercian abbot", "papal legate", "crusade commander"],
     HOLY_BLOOD_SOURCE),

    ("wiki/persons/pope-innocent-iii.md",
     "Pope Innocent III",
     [],
     ["Pope of Rome (1198–1216)"],
     HOLY_BLOOD_SOURCE),

    ("wiki/persons/jean-de-gisors.md",
     "Jean de Gisors (c.1133–1220)",
     ["Jean de Gisors"],
     ["alleged Grand Master of the Priory of Sion"],
     HOLY_BLOOD_SOURCE),

    ("wiki/persons/marie-de-negre-d-ables.md",
     "Marie de Nègre d'Ablès, Marquise de Blanchefort",
     ["Marie de Nègre d'Ablès"],
     ["French noblewoman", "wife of the Marquis de Blanchefort"],
     HOLY_BLOOD_SOURCE),

    ("wiki/persons/marie-denarnaud.md",
     "Marie Denarnaud (housekeeper)",
     ["Marie Denarnaud"],
     ["housekeeper to Bérenger Saunière"],
     HOLY_BLOOD_SOURCE),

    ("wiki/persons/henry-ii-of-england.md",
     "Henry II of England",
     [],
     ["King of England (1154–1189)"],
     HOLY_BLOOD_SOURCE),

    ("wiki/persons/philippe-ii-of-france.md",
     "Philippe II of France (Philippe Auguste)",
     ["Philippe Auguste"],
     ["King of France (1180–1223)"],
     HOLY_BLOOD_SOURCE),

    ("wiki/persons/richard-i-coeur-de-lion.md",
     "Richard I (Coeur de Lion)",
     ["Richard I", "Richard the Lionheart"],
     ["King of England (1189–1199)", "Crusader king"],
     HOLY_BLOOD_SOURCE),

    ("wiki/persons/hugues-de-payen.md",
     "Hugues de Payen (Templar founder)",
     ["Hugues de Payen"],
     ["co-founder and first Grand Master of the Knights Templar"],
     HOLY_BLOOD_SOURCE),

    ("wiki/persons/andre-de-montbard.md",
     "André de Montbard (Saint Bernard's uncle)",
     ["André de Montbard"],
     ["co-founder of the Knights Templar", "uncle of Bernard of Clairvaux"],
     HOLY_BLOOD_SOURCE),

    ("wiki/persons/hugues-count-of-champagne.md",
     "Hugues, Count of Champagne",
     [],
     ["Count of Champagne", "patron of the Knights Templar"],
     HOLY_BLOOD_SOURCE),

    ("wiki/persons/baudouin-i.md",
     "Baudouin I (first King of Jerusalem)",
     ["Baudouin I"],
     ["first King of Jerusalem (1100–1118)"],
     HOLY_BLOOD_SOURCE),

    ("wiki/persons/merovee.md",
     "Merovee (semi-legendary Frankish king)",
     ["Merovée"],
     ["semi-legendary Frankish king", "progenitor of the Merovingian dynasty"],
     HOLY_BLOOD_SOURCE),

    ("wiki/persons/clovis-i.md",
     "Clovis I (c.466–511)",
     ["Clovis I"],
     ["Merovingian king of the Franks (c.481–511)", "first Christian Frankish king"],
     HOLY_BLOOD_SOURCE),

    ("wiki/persons/jean-cocteau.md",
     "Jean Cocteau (1889–1963)",
     ["Jean Cocteau"],
     ["French poet, novelist, artist", "alleged Grand Master of the Priory of Sion"],
     HOLY_BLOOD_SOURCE),

    ("wiki/persons/claude-debussy.md",
     "Claude Debussy (1862–1918)",
     ["Claude Debussy"],
     ["French composer", "alleged Grand Master of the Priory of Sion"],
     HOLY_BLOOD_SOURCE),

    ("wiki/persons/isaac-newton.md",
     "Isaac Newton (1643–1727)",
     ["Isaac Newton"],
     ["English mathematician and physicist", "alleged Grand Master of the Priory of Sion"],
     HOLY_BLOOD_SOURCE),

    ("wiki/persons/leonardo-da-vinci.md",
     "Leonardo da Vinci (1452–1519)",
     ["Leonardo da Vinci"],
     ["Italian Renaissance polymath", "alleged Grand Master of the Priory of Sion"],
     HOLY_BLOOD_SOURCE),

    ("wiki/persons/nicolas-flamel.md",
     "Nicolas Flamel (c.1330–1418)",
     ["Nicolas Flamel"],
     ["French scribe and manuscript seller", "legendary alchemist"],
     HOLY_BLOOD_SOURCE),

    ("wiki/persons/victor-hugo.md",
     "Victor Hugo (1802–1885)",
     ["Victor Hugo"],
     ["French poet, novelist, playwright", "alleged Grand Master of the Priory of Sion"],
     HOLY_BLOOD_SOURCE),

    ("wiki/persons/nicolas-fouquet.md",
     "Nicolas Fouquet (Superintendent of Finances)",
     ["Nicolas Fouquet"],
     ["Superintendent of Finances under Louis XIV"],
     HOLY_BLOOD_SOURCE),

    ("wiki/persons/archduke-johann-von-habsburg.md",
     "Archduke Johann von Habsburg",
     [],
     ["Austrian archduke", "alleged Grand Master of the Priory of Sion"],
     HOLY_BLOOD_SOURCE),

    ("wiki/persons/louis-xiv-of-france.md",
     "Louis XIV of France",
     ["Louis XIV", "the Sun King"],
     ["King of France (1643–1715)"],
     HOLY_BLOOD_SOURCE),

    ("wiki/persons/pepin-d-heristal.md",
     "Pépin d'Héristal (Carolingian mayor of the palace)",
     ["Pépin d'Héristal", "Pepin of Herstal"],
     ["Carolingian mayor of the palace", "de facto ruler of the Frankish kingdom"],
     HOLY_BLOOD_SOURCE),

    ("wiki/persons/abbe-antoine-bigou.md",
     "Abbé Antoine Bigou",
     ["Abbé Antoine Bigou (predecessor at Rennes-le-Château)"],
     ["parish priest at Rennes-le-Château (c.1774–1790)"],
     HOLY_BLOOD_SOURCE),

    ("wiki/persons/emile-hoffet.md",
     "Émile Hoffet (Paris ecclesiastic)",
     ["Émile Hoffet"],
     ["Paris ecclesiastic and linguist"],
     HOLY_BLOOD_SOURCE),

    ("wiki/persons/simon-de-montfort.md",
     "Simon de Montfort (crusade commander)",
     ["Simon de Montfort the Elder"],
     ["military leader", "commander of the Albigensian Crusade"],
     HOLY_BLOOD_SOURCE),

    # Cooper / NWO cluster
    ("wiki/persons/william-greer.md",
     "William Greer (Secret Service driver)",
     ["William Greer"],
     ["Secret Service agent", "driver of President Kennedy's limousine"],
     COOPER_SOURCE),

    ("wiki/persons/george-hw-bush.md",
     "George H.W. Bush",
     ["George H.W. Bush", "George Bush Sr."],
     ["CIA Director", "41st President of the United States"],
     COOPER_SOURCE),

    ("wiki/persons/james-forrestal.md",
     "James Forrestal (Secretary of Defense)",
     ["James Forrestal"],
     ["first United States Secretary of Defense (1947–1949)"],
     COOPER_SOURCE),

    ("wiki/persons/gary-allen.md",
     "Gary Allen",
     [],
     ["American journalist and author"],
     ALLEN_SOURCE),

    ("wiki/persons/john-mccone.md",
     "John McCone (CIA director)",
     ["John McCone"],
     ["Director of Central Intelligence (1961–1965)"],
     COOPER_SOURCE),

    ("wiki/persons/william-casey.md",
     "William Casey (CIA director)",
     ["William Casey"],
     ["Director of Central Intelligence (1981–1987)"],
     COOPER_SOURCE),

    ("wiki/persons/james-shreve-jr.md",
     "James Shreve Jr (Project 57)",
     ["James Shreve Jr."],
     ["government official associated with Project 57"],
     JACOBS_SOURCE),

    ("wiki/persons/alfred-o-donnell.md",
     "Alfred O'Donnell (EG&G)",
     ["Alfred O'Donnell"],
     ["EG&G contractor", "associated with nuclear weapons testing"],
     JACOBS_SOURCE),

    ("wiki/persons/vannevar-bush.md",
     "Dr. Vannevar Bush",
     ["Vannevar Bush", "Vannevar Bush (Manhattan Project context)"],
     ["American engineer and science administrator", "head of OSRD during WWII"],
     COOPER_SOURCE),

    ("wiki/persons/guillermo-mendoza.md",
     "Dr. Guillermo Mendoza (botanist)",
     ["Guillermo Mendoza"],
     ["botanist"],
     JACOBS_SOURCE),

    ("wiki/persons/credo-mutwa.md",
     "Credo Mutwa",
     [],
     ["South African Zulu sangoma (shaman)", "author"],
     ICKE_SOURCE),

    # Campbell / Monroe cluster
    ("wiki/persons/bill-yost.md",
     "Bill Yost",
     [],
     ["consciousness researcher", "Monroe Institute colleague"],
     CAMPBELL_SOURCE),

    ("wiki/persons/nancy-lea-honeycutt.md",
     "Nancy Lea Honeycutt",
     [],
     ["consciousness researcher", "Monroe Institute colleague"],
     CAMPBELL_SOURCE),

    # Simulation
    ("wiki/persons/rizwan-virk.md",
     "Rizwan Virk",
     [],
     ["entrepreneur", "author", "MIT researcher"],
     VIRK_SOURCE),

    # Biblical / historical
    ("wiki/persons/jesus-of-nazareth.md",
     "Jesus of Nazareth",
     ["Jesus", "Jesus Christ", "Yeshua"],
     ["central figure of Christianity"],
     HOLY_BLOOD_SOURCE),
]

GROUP_STUBS = [
    ("wiki/groups/rockefeller-family.md",
     "Rockefeller family",
     [],
     "dynasty / family",
     COOPER_SOURCE),

    ("wiki/groups/bilderberg-group.md",
     "Bilderberg Group (Cooper)",
     ["Bilderberg Group", "Bilderberg Policy Committee (Cooper)", "Bilderberg Policy Committee"],
     "ideological_movement",
     COOPER_SOURCE),

    ("wiki/groups/majesty-twelve.md",
     "Majesty Twelve (Cooper)",
     ["Majesty Twelve", "MJ-12 (Cooper)"],
     "secret_society",
     COOPER_SOURCE),

    ("wiki/groups/jason-society.md",
     "JASON Society (Cooper)",
     ["JASON Society", "Jason Scholars (Cooper)"],
     "secret_society",
     COOPER_SOURCE),

    ("wiki/groups/knights-of-malta.md",
     "Knights of Malta (Cooper)",
     ["Knights of Malta", "Order of Malta", "Sovereign Military Order of Malta"],
     "secret_society",
     COOPER_SOURCE),

    ("wiki/groups/department-of-defense-us.md",
     "Department of Defense (US)",
     ["Department of Defense (Cooper)", "Department of Defense"],
     "polity",
     COOPER_SOURCE),

    ("wiki/groups/fema-cooper.md",
     "FEMA (Cooper)",
     ["FEMA", "Federal Emergency Management Agency (Cooper)"],
     "polity",
     COOPER_SOURCE),

    ("wiki/groups/us-navy-oni.md",
     "U.S. Navy Office of Naval Intelligence",
     ["Office of Naval Intelligence", "ONI"],
     "polity",
     COOPER_SOURCE),

    ("wiki/groups/counts-of-toulouse.md",
     "Counts of Toulouse",
     [],
     "dynasty / family",
     HOLY_BLOOD_SOURCE),

    ("wiki/groups/house-of-trencavel.md",
     "House of Trencavel",
     ["Trencavel (family)"],
     "dynasty / family",
     HOLY_BLOOD_SOURCE),

    ("wiki/groups/habsburg-lorraine.md",
     "Habsburg-Lorraine (house)",
     ["House of Habsburg-Lorraine", "Habsburg-Lorraine"],
     "dynasty / family",
     HOLY_BLOOD_SOURCE),

    ("wiki/groups/vatican-cooper.md",
     "Vatican (Cooper)",
     ["Vatican", "Holy See (Cooper)"],
     "polity",
     COOPER_SOURCE),
]

LOCATION_STUBS = [
    ("wiki/locations/jerusalem.md",
     "Jerusalem",
     ["City of David"],
     HOLY_BLOOD_SOURCE),

    ("wiki/locations/gaul-languedoc.md",
     "Gaul (southern France / Languedoc)",
     ["Gaul", "Languedoc", "southern France"],
     HOLY_BLOOD_SOURCE),

    ("wiki/locations/antarctica.md",
     "Antarctica",
     [],
     COOPER_SOURCE),

    ("wiki/locations/arques.md",
     "Arques (near Rennes-le-Château)",
     ["Arques"],
     HOLY_BLOOD_SOURCE),

    ("wiki/locations/stenay.md",
     "Stenay (Merovingian capital)",
     ["Stenay"],
     HOLY_BLOOD_SOURCE),

    ("wiki/locations/saint-sulpice-paris.md",
     "Saint-Sulpice (Paris seminary)",
     ["Saint-Sulpice", "Church of Saint-Sulpice"],
     HOLY_BLOOD_SOURCE),
]

EVENT_STUBS = [
    ("wiki/events/ufo-disclosure/may-2022-uap-congressional-hearing.md",
     "May 2022 Congressional UAP public hearing",
     ["May 2022 Congressional UAP public hearing"],
     "May 2022",
     ELIZONDO_SOURCE),
]

CONCEPT_STUBS = [
    ("wiki/concepts/consciousness-evolution-fractal-ecosystem.md",
     "Concept: Consciousness-Evolution Fractal Ecosystem",
     ["Consciousness-Evolution Fractal Ecosystem"],
     CAMPBELL_SOURCE),

    ("wiki/concepts/thought-control.md",
     "Concept: Thought Control",
     ["Thought Control (Monroe)"],
     MONROE_JOOB_SOURCE),
]

# Claims that are referenced in comparisons/source indexes but don't have dedicated pages
CAMPBELL_CLAIM_STUBS = [
    ("wiki/claims/consciousness-obe/campbell-auo-primordial-consciousness.md",
     "Claim: AUO is the primordial undifferentiated consciousness from which all reality derives",
     [],
     CAMPBELL_SOURCE),

    ("wiki/claims/consciousness-obe/campbell-aum-evolved-from-auo.md",
     "Claim: AUM is AUO evolved into low-entropy, structured, manifold consciousness",
     [],
     CAMPBELL_SOURCE),

    ("wiki/claims/consciousness-obe/campbell-consciousness-evolves-low-entropy.md",
     "Claim: Consciousness naturally evolves from high entropy to low entropy via the Fundamental Process",
     [],
     CAMPBELL_SOURCE),

    ("wiki/claims/consciousness-obe/campbell-individuated-consciousness-multiple-lives.md",
     "Claim: Individuated consciousness accumulates quality across multiple PMR lifetimes",
     [],
     CAMPBELL_SOURCE),

    ("wiki/claims/consciousness-obe/campbell-love-low-entropy-expression.md",
     "Claim: Love is technically the expression of low-entropy consciousness",
     [],
     CAMPBELL_SOURCE),

    ("wiki/claims/consciousness-obe/campbell-purpose-consciousness-quality-evolution.md",
     "Claim: The purpose of human life is consciousness quality evolution",
     [],
     CAMPBELL_SOURCE),

    ("wiki/claims/consciousness-obe/campbell-psi-acausal-outside-pmr.md",
     "Claim: Psi phenomena are acausal effects of consciousness operating outside PMR rule-set",
     [],
     CAMPBELL_SOURCE),

    ("wiki/claims/consciousness-obe/campbell-psi-uncertainty-limits-access.md",
     "Claim: The Psi Uncertainty Principle limits psi access to those who can use it constructively",
     [],
     CAMPBELL_SOURCE),

    ("wiki/claims/consciousness-obe/campbell-precognition-probable-reality-surfaces.md",
     "Claim: Precognition is access to computed probable reality surfaces by consciousness",
     [],
     CAMPBELL_SOURCE),

    ("wiki/claims/consciousness-obe/campbell-obes-npmr-access.md",
     "Claim: OBEs are consciousness accessing NPMR directly, bypassing PMR experience",
     [],
     CAMPBELL_SOURCE),

    ("wiki/claims/consciousness-obe/campbell-npmr-less-constrained-dimensional-reality.md",
     "Claim: Nonphysical Matter Reality (NPMR) is a less constrained dimensional reality within AUM",
     [],
     CAMPBELL_SOURCE),

    ("wiki/claims/consciousness-obe/campbell-pmr-virtual-reality-within-aum.md",
     "Claim: Physical Matter Reality (PMR) is a rule-set-based virtual reality within AUM's consciousness",
     [],
     CAMPBELL_SOURCE),

    ("wiki/claims/consciousness-obe/campbell-spacetime-perceptual-construct-pmr.md",
     "Claim: Space-time is a perceptual construct imposed by the PMR rule-set, not fundamental reality",
     [],
     CAMPBELL_SOURCE),

    ("wiki/claims/consciousness-obe/campbell-speed-of-light-aum-constraint.md",
     "Claim: The speed of light is a constraint evolved by AUM to define the space-time virtual reality",
     [],
     CAMPBELL_SOURCE),
]

MONROE_JOOB_CLAIM_STUBS = [
    ("wiki/claims/consciousness-obe/monroe-non-physical-existence-after-death.md",
     "Claim: Non-physical existence continues after physical death",
     [],
     MONROE_JOOB_SOURCE),

    ("wiki/claims/consciousness-obe/monroe-obes-repeatable-systematic-investigation.md",
     "Claim: Out-of-body experiences are repeatable and subject to systematic investigation",
     [],
     MONROE_JOOB_SOURCE),

    ("wiki/claims/consciousness-obe/monroe-multiple-non-physical-realms.md",
     "Claim: Multiple non-physical realms exist with distinct characteristics",
     [],
     MONROE_JOOB_SOURCE),

    ("wiki/claims/consciousness-obe/monroe-vibration-frequency-controlled-mentally.md",
     "Claim: Vibration frequency can be controlled through mental direction",
     [],
     MONROE_JOOB_SOURCE),

    ("wiki/claims/consciousness-obe/monroe-thought-determines-location-non-physical.md",
     "Claim: Thought determines location and movement in non-physical state",
     [],
     MONROE_JOOB_SOURCE),

    ("wiki/claims/consciousness-obe/monroe-person-can-be-visited-during-obe.md",
     "Claim: Person can be visited during out-of-body experience",
     [],
     MONROE_JOOB_SOURCE),

    ("wiki/claims/consciousness-obe/monroe-physical-body-re-entry-reliable.md",
     "Claim: Physical body can be re-entered reliably through specific techniques",
     [],
     MONROE_JOOB_SOURCE),

    ("wiki/claims/consciousness-obe/monroe-non-physical-perception-different.md",
     "Claim: Non-physical perception operates differently than physical senses",
     [],
     MONROE_JOOB_SOURCE),

    ("wiki/claims/consciousness-obe/monroe-locale-i-adjacent-physical.md",
     "Claim: Locale I is adjacent to physical realm",
     [],
     MONROE_JOOB_SOURCE),

    ("wiki/claims/consciousness-obe/monroe-locale-ii-iii-further-from-physical.md",
     "Claim: Locale II and III are further from physical existence",
     [],
     MONROE_JOOB_SOURCE),

    ("wiki/claims/consciousness-obe/monroe-locales-correlate-mental-states.md",
     "Claim: Locales in non-physical realm correlate with mental states",
     [],
     MONROE_JOOB_SOURCE),
]

OTHER_CLAIM_STUBS = [
    ("wiki/claims/consciousness-obe/bentov-meditation-7hz-resonance.md",
     "Meditation entrains the heart-aorta system and the brain at a 7Hz standing wave resonance",
     ["Claim: 7 Hz standing wave resonance during meditation"],
     BENTOV_SOURCE),

    ("wiki/claims/consciousness-obe/bentov-holographic-universal-information.md",
     "Universal information is stored holographically and can be retrieved by a quiet mind",
     ["Claim: Universal holographic information storage"],
     BENTOV_SOURCE),

    ("wiki/claims/consciousness-obe/bentov-consciousness-ratio-subjective-objective-time.md",
     "The level of an observer's consciousness is determined by the ratio of subjective time to objective time",
     ["Consciousness is defined by subjective time dilation relative to objective clock time"],
     BENTOV_SOURCE),

    ("wiki/claims/consciousness-obe/monroe-earth-compressed-learning-system.md",
     "Earth functions as a compressed learning system for consciousness development",
     ["Earth as a Compressed Learning System"],
     "[[Far Journeys (Monroe, 1985)]]"),

    ("wiki/claims/ufo-folklore/vallee-ufo-entities-absurd-behavior.md",
     "The absurd behavior of UFO entities keeps science away and gives the myth religious overtones",
     [],
     VALLEE_SOURCE),

    ("wiki/claims/area-51/manhattan-project-cost-28-billion-adjusted.md",
     "The Manhattan Project cost approximately $28 billion in inflation-adjusted dollars",
     ["Manhattan Project cost 28 billion adjusted for inflation"],
     JACOBS_SOURCE),
]

# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main():
    print("\n========== PHASE 1: Adding aliases to existing files ==========\n")
    for filepath, field, new_aliases in ALIAS_ADDITIONS:
        add_aliases_to_file(filepath, field, new_aliases)

    print("\n========== PHASE 2: Creating stub pages ==========\n")

    print("\n--- Persons ---")
    for args in PERSON_STUBS:
        make_person_stub(*args)

    print("\n--- Groups ---")
    for args in GROUP_STUBS:
        make_group_stub(*args)

    print("\n--- Locations ---")
    for args in LOCATION_STUBS:
        make_location_stub(*args)

    print("\n--- Events ---")
    for args in EVENT_STUBS:
        make_event_stub(*args)

    print("\n--- Concepts ---")
    for args in CONCEPT_STUBS:
        make_concept_stub(*args)

    print("\n--- Campbell claims ---")
    for path, title, aka, source in CAMPBELL_CLAIM_STUBS:
        make_claim_stub(path, title, aka, source)

    print("\n--- Monroe JOOB claims ---")
    for path, title, aka, source in MONROE_JOOB_CLAIM_STUBS:
        make_claim_stub(path, title, aka, source)

    print("\n--- Other claims ---")
    for path, title, aka, source in OTHER_CLAIM_STUBS:
        make_claim_stub(path, title, aka, source)

    print("\n========== DONE ==========\n")

if __name__ == "__main__":
    main()
