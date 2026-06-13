import re

with open("scratch/seth_speaks.txt", "r", encoding="utf-8") as f:
    text = f.read()

keywords = [
    ("coordinate points", r'(?i)coordinate\s+point|coordination\s+point'),
    ("three Christs", r'(?i)three\s+Christs'),
    ("lost religion", r'(?i)lost\s+religion|same\s+space|destroyed\s+their\s+planet'),
    ("Speakers", r'(?i)\bSpeakers\b'),
    ("inner senses", r'(?i)inner\s+sens'),
    ("All-That-Is", r'(?i)\bAll-That-Is\b|\bAll\s+That\s+Is\b'),
    ("reincarnational civilizations", r'(?i)reincarnational\s+civilization')
]

for name, pattern in keywords:
    print(f"=== Keyword: {name} ===")
    matches = list(re.finditer(pattern, text))
    print(f"Found {len(matches)} occurrences.")
    # Show first 3 occurrences with 3 lines of context
    for m in matches[:4]:
        start = m.start()
        line_num = text[:start].count('\n') + 1
        # Extract paragraph or 5 lines around the match
        lines = text[max(0, start-200):min(len(text), start+300)].split('\n')
        print(f"  Line {line_num}:")
        for l in lines[1:-1]:
            if l.strip():
                print(f"    {l.strip()}")
        print("-" * 40)
