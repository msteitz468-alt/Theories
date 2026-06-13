from pathlib import Path
import re

file_path = Path("/home/mark/Documents/Theories/raw-sources/The Simulation Hypothesis_ An MIT Computer - Rizwan Virk.txt")
text = file_path.read_text(encoding="utf-8", errors="ignore")
lines = text.splitlines()

print("Searching for the exact phrase 'conditional rendering':")
count = 0
for i, line in enumerate(lines):
    if "conditional rendering" in line.lower():
        count += 1
        print(f"Line {i+1}:")
        # print 5 lines before and after
        start = max(0, i-4)
        end = min(len(lines), i+5)
        for j in range(start, end):
            prefix = "-> " if j == i else "   "
            print(f"{prefix}{j+1}: {lines[j]}")
        print()
print(f"Total occurrences: {count}")
