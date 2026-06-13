import re

with open("scratch/stalking_the_wild_pendulum.txt", "r", encoding="utf-8") as f:
    text = f.read()

def print_contexts(query, title):
    print(f"=== {title} ===")
    matches = list(re.finditer(query, text, re.IGNORECASE))
    print(f"Found {len(matches)} occurrences.")
    for m in matches[:4]:
        start = m.start()
        # Find line number
        line_num = text[:start].count('\n') + 1
        print(f"Line {line_num}:")
        # Print a wrapped block of text around the match
        snippet = text[max(0, start-200):min(len(text), start+500)]
        # Clean up double linebreaks or double spaces
        snippet = re.sub(r'\s+', ' ', snippet)
        print(snippet)
        print("-" * 60)
    print("\n")

print_contexts(r'null\s+point|void|halt|turning\s+point', "Null Point / Turning Point")
print_contexts(r'7\s*Hz|micro-motion|sensory-motor|cardio-sympathetic|body\s+resonance', "7 Hz / Body Resonance")
print_contexts(r'subjective\s+time|objective\s+time', "Subjective vs Objective Time")
