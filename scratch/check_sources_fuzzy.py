import os
import re

raw_dir = "/home/mark/Documents/Theories/raw-sources"
wiki_sources_dir = "/home/mark/Documents/Theories/wiki/sources"

raw_files = sorted([f for f in os.listdir(raw_dir) if not f.startswith('.') and f != 'README.md' and os.path.isfile(os.path.join(raw_dir, f))])
wiki_files = sorted([f for f in os.listdir(wiki_sources_dir) if f.endswith('.md') and f != 'INDEX.md'])

# Normalize a string by keeping only lowercase letters and numbers
def normalize(s):
    return re.sub(r'[^a-z0-9]', '', s.lower())

print("=== PENDING SOURCES (NO MATCHING WIKI PAGE) ===")
pending_count = 0
for rf in raw_files:
    rf_norm = normalize(rf)
    
    # We will check if any wiki filename contains a significant keyword from the raw filename
    # Let's split raw filename by punctuation or spaces and extract keywords
    keywords = [w.lower() for w in re.split(r'[^a-zA-Z0-9]', rf) if len(w) >= 4]
    
    # Check if there is an existing wiki file that matches
    match_found = False
    for wf in wiki_files:
        wf_norm = normalize(wf)
        
        # Exact substring matches
        if "sethspeaks" in rf_norm and "seth-speaks" in wf:
            match_found = True
            break
        if "natureofpersonalreality" in rf_norm and "personal-reality" in wf:
            match_found = True
            break
        if "wildpendulum" in rf_norm and "wild-pendulum" in wf:
            match_found = True
            break
        if "sea-kings" in wf or "seakings" in wf_norm:
            if "seakings" in rf_norm or "sea-kings" in rf_norm or "hapgood" in rf_norm:
                match_found = True
                break
        if "sirius" in rf_norm and "sirius" in wf_norm:
            match_found = True
            break
        if "nonedarecallitconspiracy" in rf_norm and "none-dare-call" in wf:
            match_found = True
            break
        if "riseofhitler" in rf_norm and "rise-of-hitler" in wf:
            match_found = True
            break
            
        # Standard keyword overlap check
        wf_words = set([w.lower() for w in re.split(r'[^a-zA-Z0-9]', wf) if len(w) >= 4])
        overlap = set(keywords).intersection(wf_words)
        # If we have high overlap, it's likely a match
        if len(overlap) >= 2:
            match_found = True
            break
            
    if not match_found:
        print(f"- {rf}")
        pending_count += 1

print(f"\nTotal pending: {pending_count}")
