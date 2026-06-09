#!/usr/bin/env python3
"""
review_queue.py
Generates a prioritized list of claims needing review and writes it to
`09-indexes/review-queue.md`.

Scoring uses the fields actually defined by the schema (see Schema.md):

  - `status`        — draft | extracted | expanded | needs-review
  - `last_updated`  — YYYY-MM-DD

A claim is queued when it carries any review signal:

  - status == "needs-review"           → +3 (explicitly flagged)
  - status == "draft"                  → +1 (incomplete extraction)
  - last_updated older than the cutoff → +1 (stale)
  - confidence in (low, speculative)   → +2 (only when the optional
                                          `confidence` field is present;
                                          absence is never penalised)

Claims with no review signal are omitted, so a clean wiki yields an empty queue.

Frontmatter is parsed with PyYAML using the same tolerant `split("---", 2)`
strategy as validate_schema.py, so notes whose closing `---` is indented (an
artefact of older bulk ingests) are still read correctly. No dependency beyond
PyYAML. Run with the project venv:

    .venv/bin/python scripts/review_queue.py [wiki_root]
"""

import sys
from pathlib import Path
from datetime import datetime, date, timedelta

import yaml

# Directories that never contain wiki content (mirrors the other lint scripts).
SKIP_PARTS = {"raw-sources", "scripts", ".git", ".obsidian", ".venv", "09-indexes"}

STALE_AFTER_DAYS = 180


def read_frontmatter(md_file: Path):
    """Return the note's frontmatter dict, or {} if absent/unparseable."""
    text = md_file.read_text(encoding="utf-8", errors="ignore")
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    try:
        meta = yaml.safe_load(parts[1])
    except yaml.YAMLError:
        return {}
    return meta if isinstance(meta, dict) else {}


def _as_date(value):
    """Coerce a frontmatter date/datetime/string into a date, or None."""
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if value is None:
        return None
    try:
        return datetime.fromisoformat(str(value)).date()
    except ValueError:
        return None


def main():
    if len(sys.argv) > 1:
        wiki_root = Path(sys.argv[1]).expanduser().resolve()
    else:
        wiki_root = Path.cwd()

    cutoff = (datetime.now() - timedelta(days=STALE_AFTER_DAYS)).date()
    needs_review = []

    for md_file in wiki_root.rglob("*.md"):
        if any(part in SKIP_PARTS for part in md_file.parts):
            continue
        meta = read_frontmatter(md_file)
        # Select by type, not by folder, so misfiled claims are still caught.
        if meta.get("type") != "claim":
            continue

        status = meta.get("status", "draft")
        conf = meta.get("confidence")  # optional; not in base schema
        last_updated = _as_date(meta.get("last_updated"))

        priority = 0
        reasons = []
        if status == "needs-review":
            priority += 3
            reasons.append("status:needs-review")
        elif status == "draft":
            priority += 1
            reasons.append("status:draft")
        if conf in ("low", "speculative"):
            priority += 2
            reasons.append(f"confidence:{conf}")
        if last_updated is None or last_updated < cutoff:
            priority += 1
            reasons.append("stale")

        if priority > 0:
            lu = last_updated.isoformat() if last_updated else "unknown"
            needs_review.append(
                (priority, md_file.relative_to(wiki_root), status, lu, ",".join(reasons))
            )

    needs_review.sort(key=lambda r: (-r[0], str(r[1])))

    print("# Review Queue — Claims Needing Attention\n")
    print(f"Generated: {datetime.now().isoformat()}\n")
    print(f"Total items: {len(needs_review)}\n")

    for pri, path, status, last, reasons in needs_review[:50]:
        print(f"- [[{path.stem}]] (priority {pri}) | status: {status} | last_updated: {last} | {reasons}")

    out_path = wiki_root / "09-indexes" / "review-queue.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("# Review Queue — Claims Needing Attention\n\n")
        f.write(f"Generated: {datetime.now().isoformat()}\n\n")
        f.write(f"Total: {len(needs_review)}\n\n")
        for pri, path, status, last, reasons in needs_review:
            f.write(f"- [[{path.stem}]] (priority {pri}) | status: {status} | last_updated: {last} | {reasons}\n")
        if not needs_review:
            f.write("No claims currently need review.\n")

    print(f"\nFull queue written to {out_path}")


if __name__ == "__main__":
    main()
