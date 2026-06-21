import pathlib,re,sys,collections
APPLY="--apply" in sys.argv
root=pathlib.Path("wiki")
FM=re.compile(r'^---\n(.*?)\n---\n',re.S)
linkre=re.compile(r'\[\[([^\]|#]+)')
files=list(root.rglob("*.md"))
texts={f:f.read_text(encoding="utf-8") for f in files}
def meta_body(txt):
    m=FM.match(txt); return (m.group(1),txt[m.end():]) if m else ("",txt)
def title_of(txt,f):
    mm,_=meta_body(txt); t=re.search(r'^title:\s*"?(.*?)"?\s*$',mm,re.M)
    return t.group(1) if t else f.stem
def aliases_of(txt):
    mm,_=meta_body(txt); al=re.search(r'^aliases:\n((?:\s+-\s+.*\n)+)',mm,re.M)
    return re.findall(r'-\s+"?(.*?)"?\s*$',al.group(1),re.M) if al else []
pages={f:title_of(texts[f],f) for f in files}
# incoming counts
name2title={}
for f in files:
    name2title[pages[f].lower()]=pages[f]; name2title[f.stem.lower()]=pages[f]
    for a in aliases_of(texts[f]): name2title[a.lower()]=pages[f]
incoming=collections.Counter()
for f in files:
    for mt in linkre.finditer(texts[f]):
        tg=mt.group(1).strip().lower()
        if tg in name2title and name2title[tg]!=pages[f]: incoming[name2title[tg]]+=1
orphans=[f for f in files if incoming[pages[f]]==0 and f.name!="validation-report.md" and pages[f]!="INDEX"]

GENERIC={"plausible deniability","overhead espionage"}  # too-generic; handle via source page instead
def candidates(f):
    t=pages[f]; cands=[t]
    base=t.split(" (")[0]
    if base!=t and len(base)>=6: cands.append(base)
    for a in aliases_of(texts[f]):
        if a not in cands and len(a)>=8: cands.append(a)
    return cands

def link_spans(s):
    return [(m.start(),m.end()) for m in re.finditer(r'\[\[.*?\]\]',s)]

wired={}; unwired=[]
for f in orphans:
    done=False
    for ph in candidates(f):
        if ph.lower() in GENERIC: continue
        rx=re.compile(r'(?<![\w/])'+re.escape(ph)+r'(?![\w])')
        for g in files:
            if g==f: continue
            mm,body=meta_body(texts[g]); off=len(texts[g])-len(body)
            spans=link_spans(body)
            for m in rx.finditer(body):
                if any(a<=m.start()<b for a,b in spans): continue
                # build replacement link
                disp=m.group(0)
                rep=f"[[{pages[f]}]]" if disp==pages[f] else f"[[{pages[f]}|{disp}]]"
                newbody=body[:m.start()]+rep+body[m.end():]
                wired[f]=(g,ph,disp)
                if APPLY: texts[g]=texts[g][:off]+newbody; 
                done=True; break
            if done: break
        if done: break
    if not done: unwired.append(f)

if APPLY:
    for g in set(v[0] for v in wired.values()):
        g.write_text(texts[g],encoding="utf-8")

print(f"orphans (real): {len(orphans)}  wired via mention: {len(wired)}  unwired: {len(unwired)}")
print("\n--- WIRED (orphan <= linked from) ---")
for f,(g,ph,disp) in sorted(wired.items(), key=lambda x:str(x[0])):
    print(f"  {pages[f][:55]}\n      via '{disp}' in {g.relative_to(root)}")
print("\n--- UNWIRED (need source-page fallback) ---")
for f in unwired: print(f"  {pages[f]}   <= {f.relative_to(root)}")
