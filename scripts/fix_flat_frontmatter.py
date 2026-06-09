#!/usr/bin/env python3
"""
fix_flat_frontmatter.py
Repair notes whose YAML frontmatter has a flat (un-indented) block-sequence of
mappings — the artefact of an earlier bulk-ingest bug where `involved_actors`
items were emitted as:

    involved_actors:
    - type: group
    link: "[[X]]"

instead of the valid nested form:

    involved_actors:
      - type: group
        link: "[[X]]"

The script only rewrites a file when (a) its frontmatter currently fails to
parse and (b) it parses cleanly after the re-indent — so it can never corrupt a
file it doesn't actually fix. The note body is preserved byte-for-byte.

Run from the repo root:  python3 scripts/fix_flat_frontmatter.py wiki
"""

import re
import sys
from pathlib import Path

import yaml

SKIP_PARTS = {"raw-sources", "scripts", ".git", ".obsidian", ".venv"}
TYPE_ITEM = re.compile(r"^- type:")
LINK_KEY = re.compile(r"^link:")
# A top-level `key: value` whose value is an unquoted scalar.
TOP_SCALAR = re.compile(r"^([A-Za-z_][\w-]*): (.+)$")


def split_frontmatter(text):
    """Return (fm_lines, body_text) or (None, None) when there's no frontmatter."""
    if not text.startswith("---"):
        return None, None
    lines = text.split("\n")
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return lines[1:i], "\n".join(lines[i + 1:])
    return None, None


def quote_unsafe_scalar(line):
    """Quote a top-level scalar value that contains a colon-space (which YAML
    otherwise reads as a nested mapping), e.g. `title: Claim: X` -> `title: "Claim: X"`.
    Leaves already-quoted / flow values (", ', [, {) untouched."""
    m = TOP_SCALAR.match(line)
    if not m:
        return line
    key, value = m.group(1), m.group(2)
    if value[:1] in ('"', "'", "[", "{"):
        return line
    if ": " not in value and not value.endswith(":"):
        return line
    escaped = value.replace('\\', '\\\\').replace('"', '\\"')
    return f'{key}: "{escaped}"'


def repair(fm_lines):
    """Fix the two known frontmatter defects from earlier ingests:
    flat `- type:` / `link:` sequences, and unquoted scalars containing colons."""
    out = []
    in_block = False
    for line in fm_lines:
        if TYPE_ITEM.match(line):
            out.append("  " + line)
            in_block = True
        elif in_block and LINK_KEY.match(line):
            out.append("    " + line)
        else:
            in_block = False
            out.append(quote_unsafe_scalar(line))
    return out


def parses(fm_text):
    try:
        yaml.safe_load(fm_text)
        return True
    except yaml.YAMLError:
        return False


def fix_file(path: Path):
    """Returns 'fixed', 'ok', 'unfixable', or 'skip'."""
    text = path.read_text(encoding="utf-8")
    fm_lines, body = split_frontmatter(text)
    if fm_lines is None:
        return "skip"

    fm_text = "\n".join(fm_lines)
    if parses(fm_text):
        return "ok"

    fixed_lines = repair(fm_lines)
    fixed_fm = "\n".join(fixed_lines)
    if fixed_lines == fm_lines or not parses(fixed_fm):
        return "unfixable"

    path.write_text(f"---\n{fixed_fm}\n---\n{body}", encoding="utf-8")
    return "fixed"


def main():
    root = Path(sys.argv[1]).expanduser().resolve() if len(sys.argv) > 1 else Path.cwd()
    fixed, unfixable = [], []
    for md_file in root.rglob("*.md"):
        if any(part in SKIP_PARTS for part in md_file.parts):
            continue
        result = fix_file(md_file)
        rel = md_file.relative_to(root)
        if result == "fixed":
            fixed.append(str(rel))
        elif result == "unfixable":
            unfixable.append(str(rel))

    print(f"Fixed {len(fixed)} file(s):")
    for f in sorted(fixed):
        print(f"  + {f}")
    if unfixable:
        print(f"\nStill unparseable after re-indent ({len(unfixable)}):")
        for f in sorted(unfixable):
            print(f"  ! {f}")
    return 1 if unfixable else 0


if __name__ == "__main__":
    sys.exit(main())
