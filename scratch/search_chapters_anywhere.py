import re

with open("scratch/stalking_the_wild_pendulum.txt", "r", encoding="utf-8") as f:
    text = f.read()

lines = text.split('\n')
print("Searching for 'chapter' in lines:")
count = 0
for idx, line in enumerate(lines):
    if "chapter" in line.lower() and len(line.strip()) < 80:
        print(f"Line {idx+1}: {line.strip()}")
        count += 1
        if count > 40:
            break
