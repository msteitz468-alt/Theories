import re
import sys
import difflib
from pathlib import Path
import yaml
from check_wikilinks import iter_notes, build_index

def clean_name(s):
    # Remove text in parentheses, punctuation, lower case
    s = re.sub(r'\(.*?\)', '', s)
    s = s.lower().strip()
    s = re.sub(r'[^a-z0-9\s-]', '', s)
    return s

def main():
    wiki_root = Path.cwd()
    notes = list(iter_notes(wiki_root))
    titles, title_of = build_index(notes)
    
    # Parse broken_links.txt
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

    all_unique_broken = sorted(list({l for links in broken_by_file.values() for l in links}))
    
    # We want to map each broken link to a valid title.
    # Let's map each title to its clean version.
    titles_list = list(titles)
    clean_titles = {t: clean_name(t) for t in titles_list}
    
    suggestions = {}
    
    for link in all_unique_broken:
        clean_lnk = clean_name(link)
        
        # 1. Look for exact clean match
        exact_matches = [t for t, cl in clean_titles.items() if cl == clean_lnk]
        if len(exact_matches) == 1:
            suggestions[link] = exact_matches
            continue
        elif len(exact_matches) > 1:
            suggestions[link] = exact_matches
            continue
            
        # 2. Look for case-insensitive match (maybe clean_name was too aggressive)
        case_matches = [t for t in titles_list if t.lower() == link.lower()]
        if case_matches:
            suggestions[link] = case_matches
            continue
            
        # 3. Look for matches using difflib
        matches = difflib.get_close_matches(link, titles_list, n=3, cutoff=0.5)
        if not matches:
            # Try matching clean names
            clean_matches = difflib.get_close_matches(clean_lnk, list(clean_titles.values()), n=3, cutoff=0.5)
            # Find the original titles for these clean matches
            matches = []
            for cm in clean_matches:
                for t, cl in clean_titles.items():
                    if cl == cm:
                        matches.append(t)
            
            # Remove duplicates
            seen = set()
            matches = [x for x in matches if not (x in seen or seen.add(x))][:3]
            
        suggestions[link] = matches

    # Print mapping
    with open("scratch/clean_suggestions.txt", "w") as f:
        f.write("=== FUZZY MATCH SUGGESTIONS ===\n\n")
        for link in all_unique_broken:
            sugg = suggestions.get(link, [])
            f.write(f"Broken: [[{link}]]\n")
            if sugg:
                for s in sugg:
                    f.write(f"  -> [[{s}]]\n")
            else:
                f.write("  -> NO MATCH FOUND\n")
            f.write("\n")

        f.write("\n=== MAP BY FILE ===\n\n")
        for file, links in sorted(broken_by_file.items()):
            f.write(f"{file}:\n")
            for link in links:
                sugg = suggestions.get(link, [])
                best = sugg[0] if sugg else "???"
                f.write(f"  [[{link}]] -> [[{best}]] (all: {sugg})\n")
            f.write("\n")

if __name__ == "__main__":
    main()
