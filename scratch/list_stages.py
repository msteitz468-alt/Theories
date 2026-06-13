from pathlib import Path
import re

file_path = Path("/home/mark/Documents/Theories/raw-sources/The Simulation Hypothesis_ An MIT Computer - Rizwan Virk.txt")
text = file_path.read_text(encoding="utf-8", errors="ignore")
lines = text.splitlines()

print("Searching for 'stage' and stages of the simulation:")
count = 0
for i, line in enumerate(lines):
    # Search for lines like "Stage 1", "Stage One", "Stage 2", etc., or "ten stages"
    if re.search(r'\bstage\s+\d+\b', line.lower()) or re.search(r'\bstage\s+(one|two|three|four|five|six|seven|eight|nine|ten)\b', line.lower()):
        count += 1
        print(f"Line {i+1}: {line}")
        if count >= 30:
            print("Truncated...")
            break
