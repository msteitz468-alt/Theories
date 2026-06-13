import os
import re

raw_dir = "/home/mark/Documents/Theories/raw-sources"
wiki_sources_dir = "/home/mark/Documents/Theories/wiki/sources"

raw_files = sorted([f for f in os.listdir(raw_dir) if not f.startswith('.') and f != 'README.md' and os.path.isfile(os.path.join(raw_dir, f))])
wiki_files = sorted([f for f in os.listdir(wiki_sources_dir) if f.endswith('.md') and f != 'INDEX.md'])

# Let's read the frontmatter title of each wiki source page to match against raw file names
wiki_titles_and_authors = []
for wf in wiki_files:
    path = os.path.join(wiki_sources_dir, wf)
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    # Extract frontmatter title and author
    title_match = re.search(r'^title:\s*(.*?)$', content, re.MULTILINE)
    author_match = re.search(r'^author_or_origin:\s*(.*?)$', content, re.MULTILINE)
    
    title = title_match.group(1).strip().strip('"\'') if title_match else ""
    # If author_or_origin is a list, find all lines under it
    authors = []
    if author_match:
        auth_line = author_match.group(1).strip()
        if auth_line == "" or auth_line.startswith('['):
            # check if it's list in brackets
            authors = re.findall(r'["\'](.*?)["\']', auth_line)
        else:
            authors = [auth_line]
    else:
        # scan for indented list
        fm_match = re.search(r'^---(.*?)^---', content, re.MULTILINE | re.DOTALL)
        if fm_match:
            lines = fm_match.group(1).split('\n')
            in_author = False
            for line in lines:
                if line.startswith('author_or_origin:'):
                    in_author = True
                elif in_author and line.startswith('  - '):
                    authors.append(line.replace('  - ', '').strip().strip('"\''))
                elif in_author and (line.startswith('title:') or line.startswith('type:') or not line.startswith(' ')):
                    in_author = False
                    
    wiki_titles_and_authors.append({
        'filename': wf,
        'title': title,
        'authors': authors
    })

print(f"Total raw files: {len(raw_files)}")
print(f"Total wiki pages: {len(wiki_files)}")

not_ingested = []
ingested = []

for rf in raw_files:
    # Clean the raw file name to get keywords
    stem = os.path.splitext(rf)[0]
    # Remove things like "Anna's Archive", "z-library", brackets, etc.
    stem_clean = re.sub(r'\(.*?\)|\[.*?\]|--.*|z-library.*|1lib.*|Anna’s Archive.*', '', stem).strip()
    
    # Check if any wiki page matches
    matched = None
    for wp in wiki_titles_and_authors:
        # Check title overlap
        title_words = set(re.findall(r'\b[a-z]{4,}\b', wp['title'].lower()))
        rf_words = set(re.findall(r'\b[a-z]{4,}\b', stem_clean.lower()))
        
        # Check author match
        author_match = False
        for auth in wp['authors']:
            auth_words = set(re.findall(r'\b[a-z]{3,}\b', auth.lower()))
            if auth_words.intersection(rf_words):
                author_match = True
                break
                
        # If we have title overlap and author match (or highly significant title overlap)
        overlap = title_words.intersection(rf_words)
        if (len(overlap) >= 2 and author_match) or len(overlap) >= 3:
            matched = wp
            break
            
    # Manual overrides/checks for known mismatches
    if not matched:
        if "Conspirators" in rf and any("coleman-conspirators" in wp['filename'] for wp in wiki_titles_and_authors):
            matched = next(wp for wp in wiki_titles_and_authors if "coleman-conspirators" in wp['filename'])
        elif "Jekyll Island" in rf and any("griffin-creature" in wp['filename'] for wp in wiki_titles_and_authors):
            matched = next(wp for wp in wiki_titles_and_authors if "griffin-creature" in wp['filename'])
        elif "Behold a pale horse" in rf and any("behold-a-pale-horse" in wp['filename'] for wp in wiki_titles_and_authors):
            matched = next(wp for wp in wiki_titles_and_authors if "behold-a-pale-horse" in wp['filename'])
        elif "America's Secret Establishment" in rf and any("americas-secret-establishment" in wp['filename'] for wp in wiki_titles_and_authors):
            matched = next(wp for wp in wiki_titles_and_authors if "americas-secret-establishment" in wp['filename'])
        elif "Reality Transurfing I - V" in rf and any("reality-transurfing" in wp['filename'] for wp in wiki_titles_and_authors):
            matched = next(wp for wp in wiki_titles_and_authors if "reality-transurfing" in wp['filename'])
            
    if matched:
        ingested.append((rf, matched['filename']))
    else:
        not_ingested.append((rf, stem_clean))

print(f"\nIngested: {len(ingested)}")
print(f"Not Ingested: {len(not_ingested)}")

print("\n=== DETAILED LIST OF NOT INGESTED RAW SOURCES ===")
for rf, clean in sorted(not_ingested):
    print(f"- File: {rf}\n  (Clean Title: {clean})\n")
