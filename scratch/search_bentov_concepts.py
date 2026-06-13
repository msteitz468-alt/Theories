import re

with open("scratch/stalking_the_wild_pendulum.txt", "r", encoding="utf-8") as f:
    text = f.read()

keywords = [
    ("null point / void / halt", r'(?i)null\s+point|void|halt|turn\b|turning\s+point'),
    ("pendulum swing / oscillation", r'(?i)pendulum|oscillat'),
    ("hologram", r'(?i)hologram|holographic'),
    ("subjective / objective time ratio", r'(?i)subjective\s+time|ratio\s+of'),
    ("7 Hz resonance / heart / body resonance", r'(?i)7\s*Hz|cardio|micro-motion|resonance')
]

for name, pattern in keywords:
    print(f"=== Keyword: {name} ===")
    matches = list(re.finditer(pattern, text))
    print(f"Found {len(matches)} occurrences.")
    for m in matches[:3]:
        start = m.start()
        line_num = text[:start].count('\n') + 1
        lines = text[max(0, start-150):min(len(text), start+250)].split('\n')
        print(f"  Line {line_num}:")
        for l in lines[1:-1]:
            if l.strip():
                print(f"    {l.strip()}")
        print("-" * 40)
