import zipfile
import re
import os
from bs4 import BeautifulSoup

epub_path = "/home/mark/Documents/Theories/raw-sources/The Sirius Mystery (Robert K. G. Temple) (z-library.sk, 1lib.sk, z-lib.sk).epub"
output_txt = "/home/mark/Documents/Theories/scratch/the_sirius_mystery.txt"

print(f"Reading EPUB: {os.path.basename(epub_path)}")

with zipfile.ZipFile(epub_path, 'r') as z:
    # Find all HTML/XHTML/HTML files
    names = z.namelist()
    html_files = [n for n in names if n.endswith(('.html', '.xhtml', '.htm', '.xml'))]
    # Sort them to maintain book order (usually sorted alphabetically or by manifest order)
    # Let's inspect the names first
    html_files.sort()
    
    # We can filter out files that are not content, e.g. cover page, toc page, etc. if needed
    # but printing them in alphabetical order is usually safe or we can extract all of them
    full_text = []
    for name in html_files:
        if 'toc' in name.lower() or 'cover' in name.lower():
            # keep them anyway to capture TOC
            pass
        try:
            content = z.read(name)
            soup = BeautifulSoup(content, 'html.parser')
            # Extract text
            text = soup.get_text()
            # Normalize whitespace
            text = re.sub(r'\n\s*\n', '\n\n', text)
            full_text.append(f"\n\n=== FILE: {name} ===\n\n")
            full_text.append(text)
        except Exception as e:
            print(f"Error reading {name}: {e}")

with open(output_txt, 'w', encoding='utf-8') as f:
    f.write(''.join(full_text))

print(f"Extraction complete! Saved to {output_txt}. Total size: {os.path.getsize(output_txt)} bytes.")
