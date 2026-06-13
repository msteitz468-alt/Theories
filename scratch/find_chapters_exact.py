import re

with open("scratch/seth_speaks.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Let's find matches for Chapter followed by numbers
matches = re.finditer(r'(?i)^\s*(CHAPTER\s+\d+|APPENDIX)\b', text, re.MULTILINE)

for m in matches:
    start_pos = m.start()
    # Find line number
    line_num = text[:start_pos].count('\n') + 1
    # print line and the next 3 lines
    lines = text[start_pos:start_pos+300].split('\n')
    print(f"Line {line_num}: {lines[0]}")
    for l in lines[1:5]:
        if l.strip():
            print(f"   {l.strip()}")
