import re

with open("scratch/seth_speaks.txt", "r", encoding="utf-8") as f:
    text = f.read()

def print_contexts(query, title):
    print(f"=== {title} ===")
    for m in re.finditer(query, text, re.IGNORECASE):
        start = m.start()
        # Find line number
        line_num = text[:start].count('\n') + 1
        print(f"Line {line_num}:")
        # Print lines around the match
        snippet = text[max(0, start-300):min(len(text), start+500)]
        print(snippet)
        print("="*60)

print_contexts(r'coordinate\s+point|coordination\s+point', "Coordinate / Coordination Points")
print_contexts(r'three\s+Christs', "Three Christs")
print_contexts(r'lost\s+religion|destroyed\s+their\s+planet|destroyed\s+it\s+through\s+their\s+own\s+error', "Lost Civilization/Religion")
