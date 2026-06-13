import sys
from pathlib import Path
import yaml
from check_wikilinks import iter_notes, build_index

def main():
    wiki_root = Path.cwd()
    notes = list(iter_notes(wiki_root))
    titles, title_of = build_index(notes)
    
    # We want to output all files with their actual title and their aliases
    # to help us map the broken ones
    with open("scratch/available_titles.txt", "w") as f:
        f.write("=== FILES AND TITLES ===\n")
        for md_file, meta, _ in sorted(notes, key=lambda x: x[0]):
            title = meta.get("title") or md_file.stem
            aliases = []
            for key in ("also_known_as", "aliases"):
                aliases.extend(meta.get(key) or [])
            f.write(f"File: {md_file.relative_to(wiki_root)}\n")
            f.write(f"  Title: {title}\n")
            if aliases:
                f.write(f"  Aliases: {aliases}\n")
            f.write("\n")
            
        f.write("\n=== ALL REGISTERED TITLES/ALIASES ===\n")
        for t in sorted(list(titles)):
            f.write(f"- {t}\n")

if __name__ == "__main__":
    main()
