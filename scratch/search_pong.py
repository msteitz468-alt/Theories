from pathlib import Path

file_path = Path("/home/mark/Documents/Theories/raw-sources/The Simulation Hypothesis_ An MIT Computer - Rizwan Virk.txt")
text = file_path.read_text(encoding="utf-8", errors="ignore")
lines = text.splitlines()

print("Searching for 'Pong' in file:")
count = 0
for i, line in enumerate(lines):
    if "Pong" in line:
        count += 1
        print(f"Line {i+1}: {line}")
        if count >= 10:
            print("Truncated...")
            break
print(f"Total occurrences of 'Pong': {count}")
