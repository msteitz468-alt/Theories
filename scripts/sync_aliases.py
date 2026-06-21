"""Sync Obsidian-native `aliases:` on every wiki page.

WHY: pages use kebab-case FILENAMES but links use the `title:` (with spaces).
Obsidian resolves [[links]] only by filename or the `aliases:` field — NOT by
the `title:` frontmatter — so without this, title-based links open empty notes.
This script ensures each page's `aliases:` contains its title + any
`also_known_as` / pre-existing alias values (de-duplicated, single block).

RUN AFTER EVERY INGEST:  .venv/bin/python scripts/sync_aliases.py --apply
(omit --apply for a dry run). Idempotent.
"""
import pathlib, re, sys, yaml
DRY = "--apply" not in sys.argv
root=pathlib.Path("wiki")
FM=re.compile(r'^---\n(.*?)\n---\n', re.S)
def yq(s): return '"'+str(s).replace('\\','\\\\').replace('"','\\"')+'"'
def strip_q(v):
    v=v.strip()
    if len(v)>=2 and v[0] in '"\'' and v[-1]==v[0]: v=v[1:-1]
    return v

changed=0; skipped=0; failed=0
for f in sorted(root.rglob("*.md")):
    txt=f.read_text(encoding="utf-8"); m=FM.match(txt)
    if not m: skipped+=1; continue
    fm=m.group(1); body=txt[m.end():]
    try: meta=yaml.safe_load(fm) or {}
    except Exception: failed+=1; continue
    title=meta.get("title") or f.stem
    aka=meta.get("also_known_as") or []
    if isinstance(aka,str): aka=[aka]
    lines=fm.split('\n')
    collected=[]; keep=[]; i=0
    while i < len(lines):
        ln=lines[i]
        mblock=re.match(r'^aliases:\s*$',ln)
        minline_br=re.match(r'^aliases:\s*\[(.*)\]\s*$',ln)
        minline_sc=re.match(r'^aliases:\s*(\S.*)$',ln)
        if mblock:
            i+=1
            while i<len(lines) and re.match(r'^\s+-\s+',lines[i]):
                collected.append(strip_q(re.sub(r'^\s+-\s+','',lines[i]))); i+=1
            continue
        if minline_br:
            for x in minline_br.group(1).split(','):
                if x.strip(): collected.append(strip_q(x))
            i+=1; continue
        if minline_sc:
            val=minline_sc.group(1)
            for x in val.split(','):
                if x.strip(): collected.append(strip_q(x))
            i+=1; continue
        keep.append(ln); i+=1
    clean=[]
    for v in [title]+list(aka)+collected:
        v=str(v).strip()
        if not v or '\\"' in v: continue
        if v not in clean: clean.append(v)
    ti=next((k for k,ln in enumerate(keep) if re.match(r'^title:',ln)),0)
    block=['aliases:']+[f'  - {yq(v)}' for v in clean]
    keep[ti+1:ti+1]=block
    new="---\n"+"\n".join(keep)+"\n---\n"+body
    if new!=txt:
        if not DRY: f.write_text(new,encoding="utf-8")
        changed+=1
print(f"{'DRY ' if DRY else ''}changed={changed} skipped={skipped} failed={failed}")
