import os
import re

raw_dir = "/home/mark/Documents/Theories/raw-sources"
wiki_sources_dir = "/home/mark/Documents/Theories/wiki/sources"
index_path = "/home/mark/Documents/Theories/wiki/sources/INDEX.md"

# List files in raw-sources
raw_files = []
for f in os.listdir(raw_dir):
    if f.startswith('.') or f == 'README.md' or os.path.isdir(os.path.join(raw_dir, f)):
        continue
    raw_files.append(f)

# Read INDEX.md
with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

# Read existing markdown source files in wiki/sources
wiki_source_files = [f for f in os.listdir(wiki_sources_dir) if f.endswith('.md') and f != 'INDEX.md']

print(f"Total raw files: {len(raw_files)}")
print(f"Total wiki source pages: {len(wiki_source_files)}")

# Let's write a matching heuristic or print them for comparison
print("\n=== RAW FILES & THEIR INGEST STATUS ===")
ingested = []
not_ingested = []

for raw in sorted(raw_files):
    # Try to find a matches in INDEX.md or wiki_source_files
    # We can clean up the name to see if it appears
    # For example, "Above Top Secret - Timothy Good.txt" -> "Above Top Secret" or "Good"
    # Or check if raw filename stem exists in wiki_source_files with some variation
    match_found = False
    
    # We will search the filename stem in INDEX.md
    stem = os.path.splitext(raw)[0]
    # Simple word list match in INDEX.md
    words = re.findall(r'\b[A-Za-z0-9]{4,}\b', stem)
    # Filter out junk words
    ignore_words = {'annas', 'archive', 'library', 'epub', 'mobi', 'pdf', 'books', 'publishing', 'edition', 'translation', 'edited', 'with', 'from', 'sksk', 'sk1lib'}
    words = [w for w in words if w.lower() not in ignore_words]
    
    # Check if stem or parts of it appear in INDEX.md
    # Also check if any wiki source file contains author or title keywords
    matched_file = None
    for wsf in wiki_source_files:
        wsf_stem = os.path.splitext(wsf)[0]
        # count matching words
        wsf_words = set(re.findall(r'\b[a-z0-9]{4,}\b', wsf_stem.lower()))
        raw_words = set(w.lower() for w in words)
        overlap = wsf_words.intersection(raw_words)
        if len(overlap) >= 2:
            match_found = True
            matched_file = wsf
            break
            
    if not match_found:
        # Check if the title or author matches INDEX.md text
        # Let's search for some distinct words in INDEX.md
        for w in words:
            if len(w) > 5 and w in index_content:
                # verify with another word
                other_words = [ow for ow in words if ow != w]
                if any(ow in index_content for ow in other_words):
                    match_found = True
                    break
                    
    if match_found:
        ingested.append((raw, matched_file))
    else:
        not_ingested.append(raw)

print(f"Ingested count: {len(ingested)}")
print(f"Not ingested count: {len(not_ingested)}")

print("\n--- NOT INGESTED RAW SOURCES ---")
for f in not_ingested:
    print(f"- {f}")

print("\n--- INGESTED RAW SOURCES (SAMPLE MATCHES) ---")
for r, w in ingested[:10]:
    print(f"- {r} -> {w}")
