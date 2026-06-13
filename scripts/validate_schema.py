#!/usr/bin/env python3
"""
validate_schema.py
Validates all Markdown notes in the wiki against the historical LLM wiki schema
defined in Schema.md.

Checks each note's YAML frontmatter for: a valid `type`, the required fields for
that type, a valid `status` value (where present), and well-formed `last_updated`
dates. Malformed YAML frontmatter is reported as an error.

No third-party dependencies beyond PyYAML.
"""

import sys
from pathlib import Path
from datetime import datetime

import yaml

# --- Schema (mirrors Schema.md) --------------------------------------------

VALID_TYPES = {
    "claim", "event", "group", "person", "source",
    "location", "period", "concept", "controversy",
    "comparison", "query", "phenomenon",
}

# Claim status enum from Schema.md ("status: draft | extracted | expanded | needs-review").
VALID_STATUS = {"draft", "extracted", "expanded", "needs-review"}

# Fields every typed note should carry.
COMMON_FIELDS = ["title", "type", "last_updated", "tags"]

# Type-specific required fields, per the frontmatter templates in Schema.md.
REQUIRED_FIELDS = {
    "claim": COMMON_FIELDS + ["date_or_period", "source_attribution", "status"],
    # `participants` is part of the event template but is frequently and
    # acceptably empty across the corpus, so it is recommended, not required.
    "event": COMMON_FIELDS + ["date_start"],
    "group": COMMON_FIELDS + ["category"],
    "person": COMMON_FIELDS + ["roles"],
    "source": COMMON_FIELDS + ["source_type", "author_or_origin"],
    "location": COMMON_FIELDS,
    "period": COMMON_FIELDS + ["start_date"],
    "concept": COMMON_FIELDS,
    "controversy": COMMON_FIELDS + ["text_locus", "positions_presented"],
    "comparison": COMMON_FIELDS,
    "query": COMMON_FIELDS,
    "phenomenon": COMMON_FIELDS + ["locations", "associated_claims"],
}

SKIP_PARTS = {"raw-sources", "scripts", ".git", ".obsidian", ".venv", "00-schema", "09-indexes"}


def parse_frontmatter(md_file: Path):
    """Return (metadata_dict, error_str). metadata is None when unparseable."""
    text = md_file.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None, "no YAML frontmatter (file does not start with '---')"
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, "unterminated YAML frontmatter (missing closing '---')"
    try:
        meta = yaml.safe_load(parts[1])
    except yaml.YAMLError as e:
        return None, f"invalid YAML frontmatter: {e}"
    if meta is None:
        return {}, None
    if not isinstance(meta, dict):
        return None, "frontmatter is not a mapping"
    return meta, None


def load_all_notes(wiki_root: Path):
    notes = []
    for md_file in wiki_root.rglob("*.md"):
        if any(part in SKIP_PARTS for part in md_file.parts):
            continue
        # Files without any frontmatter are navigation/index pages (e.g.
        # INDEX.md, README.md), not typed notes — the schema does not apply.
        if not md_file.read_text(encoding="utf-8").startswith("---"):
            continue
        meta, error = parse_frontmatter(md_file)
        notes.append((md_file, meta, error))
    return notes


def validate_note(meta):
    issues = []

    if "type" not in meta:
        issues.append("Missing required field: type")
        return issues

    ntype = meta["type"]
    if ntype not in VALID_TYPES:
        issues.append(f"Invalid type: {ntype}")
        return issues

    for field in REQUIRED_FIELDS.get(ntype, COMMON_FIELDS):
        value = meta.get(field)
        if value is None or value == "" or value == []:
            issues.append(f"Missing or empty required field for {ntype}: {field}")

    if "status" in meta and meta["status"] not in VALID_STATUS:
        issues.append(
            f"Invalid status value: {meta['status']} "
            f"(expected one of {sorted(VALID_STATUS)})"
        )

    lu = meta.get("last_updated")
    if lu is not None:
        # PyYAML may parse an unquoted YYYY-MM-DD into a datetime.date.
        try:
            datetime.fromisoformat(str(lu))
        except ValueError:
            issues.append(f"last_updated is not an ISO date (YYYY-MM-DD): {lu}")

    return issues


def main():
    if len(sys.argv) > 1:
        wiki_root = Path(sys.argv[1]).expanduser().resolve()
    else:
        wiki_root = Path.cwd()

    print(f"Validating wiki at: {wiki_root}")
    notes = load_all_notes(wiki_root)

    all_issues = {}
    parse_errors = {}
    type_counts = {}
    status_counts = {}

    for md_file, meta, error in notes:
        rel_path = str(md_file.relative_to(wiki_root))
        if error:
            parse_errors[rel_path] = error
            continue

        ntype = meta.get("type", "unknown")
        type_counts[ntype] = type_counts.get(ntype, 0) + 1
        st = meta.get("status")
        if st is not None:
            status_counts[st] = status_counts.get(st, 0) + 1

        issues = validate_note(meta)
        if issues:
            all_issues[rel_path] = issues

    print("\n" + "=" * 60)
    print("VALIDATION REPORT")
    print("=" * 60)
    print(f"Total notes scanned: {len(notes)}")

    print("\nBy type:")
    for t, count in sorted(type_counts.items()):
        print(f"  {t:12} : {count}")

    if status_counts:
        print("\nBy status:")
        for s, count in sorted(status_counts.items()):
            print(f"  {s:12} : {count}")

    if parse_errors:
        print(f"\nFiles with unparseable frontmatter: {len(parse_errors)}")
        for path, error in sorted(parse_errors.items()):
            print(f"\n- {path}")
            print(f"    • {error}")

    if all_issues:
        print(f"\nFiles with schema issues: {len(all_issues)}")
        for path, issues in sorted(all_issues.items()):
            print(f"\n- {path}")
            for issue in issues:
                print(f"    • {issue}")

    if not parse_errors and not all_issues:
        print("\nNo schema issues found. Wiki is clean.")

    report_path = wiki_root / "09-indexes" / "validation-report.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"# Wiki Validation Report — {datetime.now().isoformat()}\n\n")
        f.write(f"Total notes: {len(notes)}\n\n")
        if parse_errors:
            f.write("## Frontmatter Parse Errors\n\n")
            for path, error in sorted(parse_errors.items()):
                f.write(f"### {path}\n- {error}\n\n")
        if all_issues:
            f.write("## Schema Issues\n\n")
            for path, issues in sorted(all_issues.items()):
                f.write(f"### {path}\n")
                for issue in issues:
                    f.write(f"- {issue}\n")
                f.write("\n")
        if not parse_errors and not all_issues:
            f.write("All notes pass schema validation.\n")

    print(f"\nReport written to: {report_path}")

    # Exit non-zero when problems are found, so the script is CI-friendly.
    return 1 if (parse_errors or all_issues) else 0


if __name__ == "__main__":
    sys.exit(main())
