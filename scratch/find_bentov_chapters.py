import re

with open("scratch/stalking_the_wild_pendulum.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Find occurrences of Chapter or CHAPTER followed by numbers or names
matches = re.finditer(r'(?i)^\s*(CHAPTER\s+\d+|PART\s+(ONE|TWO|THREE))\b', text, re.MULTILINE)

for m in matches:
    start_pos = m.start()
    line_num = text[:start_pos].count('\n') + 1
    lines = text[start_pos:start_pos+300].split('\n')
    print(f"Line {line_num}: {lines[0]}")
    for l in lines[1:5]:
        if l.strip():
            print(f"   {l.strip()}")
