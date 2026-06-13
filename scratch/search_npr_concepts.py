import re

with open("scratch/nature_of_personal_reality.txt", "r", encoding="utf-8") as f:
    text = f.read()

keywords = [
    ("point of power", r'(?i)point\s+of\s+power\s+is\s+in\s+the\s+present|point\s+of\s+power'),
    ("natural grace", r'(?i)natural\s+grace|state\s+of\s+grace'),
    ("natural hypnosis", r'(?i)natural\s+hypnosis'),
    ("conscious mind", r'(?i)conscious\s+mind')
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
