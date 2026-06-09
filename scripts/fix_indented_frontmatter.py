#!/usr/bin/env python3
"""
fix_indented_frontmatter.py
Repair notes whose frontmatter *closing* fence and body were emitted with a
uniform leading indent — an artefact of an earlier bulk ingest. Affected files
look like:

    ---
    title: ...
    type: claim
    ...
    tags: [...]
        ---
        ## Claim Statement

        Body text...

The opening `---` and the YAML keys sit at column 0 (so PyYAML's tolerant
`split("---", 2)` still reads them), but the closing `---` is indented and the
entire body is indented by the same amount. In Obsidian a 4-space-indented body
renders as one big code block, and stricter parsers (python-frontmatter) fail to
detect the frontmatter at all.

The fix removes that common indent from the closing fence and every body line,
preserving *relative* indentation (nested lists keep their extra spaces) and the
note's trailing newline. The YAML block between the fences is left byte-for-byte
unchanged.

Safety: a file is only rewritten when (a) its closing fence is actually indented,
(b) the YAML block parses as a mapping, and (c) after dedent the closing fence is
exactly `---`. Anything else is reported, not touched.

Dry-run by default; pass --apply to write changes.

    .venv/bin/python scripts/fix_indented_frontmatter.py [wiki_root] [--apply]
"""

import sys
from pathlib import Path

import yaml

SKIP_PARTS = {"raw-sources", "scripts", ".git", ".obsidian", ".venv"}


def leading_spaces(line):
    """Number of leading space characters (tabs disqualify -> returns None)."""
    n = 0
    for ch in line:
        if ch == " ":
            n += 1
        elif ch == "\t":
            return None  # tab indentation: refuse to guess
        else:
            break
    return n


def analyze(text):
    """Return (frontmatter_lines, fence_idx, indent, lines) for an affected file,
    or None when the file is absent of the defect / not frontmatter."""
    if not text.startswith("---"):
        return None
    lines = text.split("\n")
    if lines[0].strip() != "---":
        return None

    # First line after the opening whose stripped value is the closing fence.
    fence_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            fence_idx = i
            break
    if fence_idx is None:
        return None

    fence_line = lines[fence_idx]
    if fence_line == "---":
        return None  # well-formed close, nothing to do

    indent = leading_spaces(fence_line)
    if not indent:  # 0, or None (tabs)
        return None

    return lines[1:fence_idx], fence_idx, indent, lines


def dedent_from(lines, indent):
    """Strip up to `indent` leading spaces from each line."""
    out = []
    for ln in lines:
        j = 0
        while j < indent and j < len(ln) and ln[j] == " ":
            j += 1
        out.append(ln[j:])
    return out


def fix_file(path: Path):
    """Returns 'fixed', 'would-fix', 'ok', or 'unfixable'."""
    text = path.read_text(encoding="utf-8")
    result = analyze(text)
    if result is None:
        return "ok", text
    fm_lines, fence_idx, indent, lines = result

    # The YAML block must be a valid mapping before we touch anything.
    try:
        meta = yaml.safe_load("\n".join(fm_lines))
    except yaml.YAMLError:
        return "unfixable", text
    if not isinstance(meta, dict):
        return "unfixable", text

    region = dedent_from(lines[fence_idx:], indent)
    if region[0] != "---":
        return "unfixable", text  # dedent did not normalize the fence

    new_lines = [lines[0]] + fm_lines + region
    new_text = "\n".join(new_lines)
    if new_text == text:
        return "ok", text
    return "fixed", new_text


def main():
    args = [a for a in sys.argv[1:]]
    apply = "--apply" in args
    args = [a for a in args if a != "--apply"]
    root = Path(args[0]).expanduser().resolve() if args else Path.cwd()

    fixed, unfixable = [], []
    for md_file in root.rglob("*.md"):
        if any(part in SKIP_PARTS for part in md_file.parts):
            continue
        status, new_text = fix_file(md_file)
        rel = str(md_file.relative_to(root))
        if status == "fixed":
            fixed.append(rel)
            if apply:
                md_file.write_text(new_text, encoding="utf-8")
        elif status == "unfixable":
            unfixable.append(rel)

    verb = "Fixed" if apply else "Would fix"
    print(f"{verb} {len(fixed)} file(s):")
    for f in sorted(fixed):
        print(f"  + {f}")
    if unfixable:
        print(f"\nIndented fence but YAML/dedent check failed ({len(unfixable)}):")
        for f in sorted(unfixable):
            print(f"  ! {f}")
    if not apply and fixed:
        print("\n(dry run — re-run with --apply to write these changes)")
    return 1 if unfixable else 0


if __name__ == "__main__":
    sys.exit(main())
