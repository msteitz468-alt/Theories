"""Add bidirectional "## Cross-source syntheses" backlinks.

Inverts every synthesis page (wiki/comparisons, wiki/controversies, wiki/queries)
and appends, to each source/concept/person/group page they cite, a section listing
the synthesis pages that reference it. Idempotent.

RUN AFTER ADDING/EDITING SYNTHESIS PAGES:
  .venv/bin/python scripts/backlink_syntheses.py --apply   (omit --apply for dry run)
"""
import pathlib, re, sys, collections
DRY = "--apply" not in sys.argv
root=pathlib.Path("wiki")
FM=re.compile(r'^---\n(.*?)\n---\n', re.S)
linkre=re.compile(r'\[\[([^\]|#]+)')

# title -> (path, kind)
title2path={}
def title_of(f):
    m=FM.match(f.read_text(encoding="utf-8"))
    if m:
        t=re.search(r'^title:\s*"?(.*?)"?\s*$',m.group(1),re.M)
        if t: return t.group(1)
    return f.stem
allmd=list(root.rglob("*.md"))
for f in allmd:
    title2path[title_of(f)]=(f, f.parts[1] if len(f.parts)>1 else "")

synth_dirs={"comparisons","controversies","queries"}
synth_files=[f for f in allmd if (len(f.parts)>1 and f.parts[1] in synth_dirs)]

# invert: target page title -> set(synthesis titles), only for source/concept targets
backlinks=collections.defaultdict(set)
for sf in synth_files:
    st=title_of(sf)
    txt=sf.read_text(encoding="utf-8")
    for m in linkre.finditer(txt):
        tgt=m.group(1).strip()
        if tgt in title2path:
            _,kind=title2path[tgt]
            if kind in ("sources","concepts","groups","persons"):
                backlinks[tgt].add(st)

MARK="## Cross-source syntheses"
changed=0; per_kind=collections.Counter()
for tgt, synths in backlinks.items():
    f,kind=title2path[tgt]
    txt=f.read_text(encoding="utf-8")
    body=FM.sub('',txt,count=1)
    block=f"{MARK}\n\nThis page is discussed in these cross-source synthesis pages:\n\n"+"\n".join(f"- [[{s}]]" for s in sorted(synths))+"\n"
    if MARK in txt:
        new=re.sub(MARK+r".*?(?=\n## |\Z)", block, txt, flags=re.S)
    else:
        new=txt.rstrip()+"\n\n"+block
    if new!=txt:
        if not DRY: f.write_text(new,encoding="utf-8")
        changed+=1; per_kind[kind]+=1
print(f"{'DRY ' if DRY else ''}pages getting backlink section: {changed}")
print("  by kind:", dict(per_kind))
print(f"  synthesis pages scanned: {len(synth_files)}")
