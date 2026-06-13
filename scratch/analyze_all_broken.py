from pathlib import Path
import yaml
import re
from check_wikilinks import iter_notes, build_index

def main():
    wiki_root = Path.cwd()
    notes = list(iter_notes(wiki_root))
    titles, title_of = build_index(notes)
    
    # Read broken_links.txt to see the exact files and targets
    broken_links_file = wiki_root / "scratch/broken_links.txt"
    if not broken_links_file.exists():
        print("broken_links.txt not found!")
        return

    content = broken_links_file.read_text(encoding="utf-8")
    
    current_file = None
    broken_by_file = {}
    for line in content.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.endswith(".md:"):
            current_file = line[:-1]
            broken_by_file[current_file] = []
        elif line.startswith("-> [[") and line.endswith("]] (missing)"):
            link = line[5:-12]
            if current_file:
                broken_by_file[current_file].append(link)

    unique_broken = sorted(list({lnk for links in broken_by_file.values() for lnk in links}))
    print(f"Total unique broken link targets: {len(unique_broken)}")
    
    # Let's write a mapping table
    # We want to check:
    # 1. Is there a page with the same name if we change case/punctuation?
    # 2. Is there a page with a slightly different name?
    # 3. Are there files in wiki/ that have the exact target name in their title?
    
    print("\n--- Analysing unique broken links ---")
    for link in unique_broken:
        # Let's find pages that have this string in their content or filenames
        # to see what they are trying to link to.
        # Find files matching the target:
        matches = []
        for t in titles:
            t_low = t.lower()
            lnk_low = link.lower()
            if t_low == lnk_low:
                matches.append(t)
            elif len(t) > 3 and (t_low in lnk_low or lnk_low in t_low):
                matches.append(t)
        print(f"Broken: {link}")
        print(f"  Matches in registered titles: {matches[:10]}")
        
if __name__ == "__main__":
    main()
