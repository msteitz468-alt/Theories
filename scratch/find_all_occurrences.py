from pathlib import Path

file_path = Path("/home/mark/Documents/Theories/raw-sources/The Simulation Hypothesis_ An MIT Computer - Rizwan Virk.txt")
text = file_path.read_text(encoding="utf-8", errors="ignore")
lines = text.splitlines()

target = "Computer Games: From Pong to MMORPGs"
print(f"Occurrences of '{target}':")
for i, line in enumerate(lines):
    if target in line:
        print(f"Line {i+1}: {line}")
        # print context
        start = max(0, i-2)
        end = min(len(lines), i+3)
        for j in range(start, end):
            print(f"  {j+1}: {lines[j]}")
        print()
