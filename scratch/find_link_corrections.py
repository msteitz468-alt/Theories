import re
import sys
from pathlib import Path
import yaml
from check_wikilinks import iter_notes, build_index

def normalize(s):
    # Normalize by lowercase and removing punctuation, spaces, dashes
    return re.sub(r'[^a-z0-9]', '', s.lower())

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
    
    # Simple parser for broken_links.txt
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

    # Let's find matches
    normalized_titles = {normalize(t): t for t in titles}
    
    # We will write suggestions to a file
    with open("scratch/link_suggestions.txt", "w") as f:
        f.write("=== SUGGESTIONS FOR BROKEN LINKS ===\n\n")
        
        all_unique_broken = set()
        for file, links in broken_by_file.items():
            for link in links:
                all_unique_broken.add(link)
                
        suggestions_map = {}
        for link in sorted(all_unique_broken):
            norm_link = normalize(link)
            
            # 1. Exact match normalized
            if norm_link in normalized_titles:
                suggestions_map[link] = [normalized_titles[norm_link]]
                continue
                
            # 2. Substring match
            matches = []
            for norm_t, t in normalized_titles.items():
                if norm_link in norm_t or norm_t in norm_link:
                    matches.append(t)
            
            # Sort matches by length difference
            matches.sort(key=lambda x: abs(len(x) - len(link)))
            suggestions_map[link] = matches[:5]
            
        for link, matches in sorted(suggestions_map.items()):
            f.write(f"Broken: [[{link}]]\n")
            if matches:
                f.write(f"  Suggestions:\n")
                for m in matches:
                    f.write(f"    - [[{m}]]\n")
            else:
                f.write(f"  Suggestions: None\n")
            f.write("\n")
            
        f.write("\n=== DETAILED MAPPING PER FILE ===\n\n")
        for file, links in sorted(broken_by_file.items()):
            f.write(f"{file}:\n")
            for link in links:
                matches = suggestions_map.get(link, [])
                best = matches[0] if matches else "???"
                f.write(f"  [[{link}]] -> [[{best}]] (choices: {matches})\n")
            f.write("\n")

if __name__ == "__main__":
    main()
