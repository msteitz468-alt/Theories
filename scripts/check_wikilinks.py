#!/usr/bin/env python3
"""
check_wikilinks.py
Extracts all [[wikilinks]] from the wiki and reports broken ones (targets with
no matching note title or alias). Also detects orphan notes (no incoming links).

Titles are resolved by a note's `title` frontmatter field (falling back to the
filename stem), plus any alternate names in `also_known_as` / `aliases`.

No third-party dependencies beyond PyYAML.
"""

import re
import sys
from pathlib import Path
from collections import defaultdict

import yaml

WIKILINK_RE = re.compile(r'\[\[([^\]|#]+)(?:\|[^\]]+)?(?:#[^\]]+)?\]\]')
SKIP_PARTS = {"raw-sources", "scripts", ".git", ".obsidian", ".venv"}
# Documentation files (not wiki notes); their [[...]] are template examples.
SKIP_NAMES = {"Schema.md", "AGENTS.md", "README.md"}


def read_frontmatter(md_file: Path):
    """Return the note's frontmatter dict, or {} if absent/unparseable."""
    text = md_file.read_text(encoding="utf-8", errors="ignore")
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    try:
        meta = yaml.safe_load(parts[1])
    except yaml.YAMLError:
        return {}, text
    return (meta if isinstance(meta, dict) else {}), text


def iter_notes(wiki_root: Path):
    for md_file in wiki_root.rglob("*.md"):
        if any(part in SKIP_PARTS for part in md_file.parts):
            continue
        if md_file.name in SKIP_NAMES:
            continue
        meta, text = read_frontmatter(md_file)
        yield md_file, meta, text


def build_index(notes):
    titles = set()
    title_of = {}
    for md_file, meta, _ in notes:
        title = meta.get("title") or md_file.stem
        titles.add(title)
        title_of[md_file] = title
        for key in ("also_known_as", "aliases"):
            for alias in (meta.get(key) or []):
                titles.add(str(alias))
    return titles, title_of


def main():
    wiki_root = Path(sys.argv[1]).expanduser().resolve() if len(sys.argv) > 1 else Path.cwd()

    print("Building title index...")
    notes = list(iter_notes(wiki_root))
    titles, title_of = build_index(notes)
    print(f"Found {len(titles)} unique titles/aliases across {len(notes)} notes")

    print("Scanning for broken wikilinks...")
    broken = defaultdict(set)
    incoming = defaultdict(int)
    for md_file, _, text in notes:
        for match in WIKILINK_RE.finditer(text):
            target = match.group(1).strip()
            if target in titles:
                incoming[target] += 1
            else:
                broken[str(md_file.relative_to(wiki_root))].add(target)

    if broken:
        total = sum(len(v) for v in broken.values())
        print(f"\nBroken wikilinks: {total} in {len(broken)} file(s):")
        for file, links in sorted(broken.items()):
            print(f"\n{file}:")
            for link in sorted(links):
                print(f"  -> [[{link}]] (missing)")
    else:
        print("\nNo broken wikilinks detected.")

    orphans = sorted(
        title_of[mf] for mf, _, _ in notes if incoming.get(title_of[mf], 0) == 0
    )
    print(f"\nOrphan notes (no incoming links): {len(orphans)}")
    for title in orphans:
        print(f"  - {title}")

    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
