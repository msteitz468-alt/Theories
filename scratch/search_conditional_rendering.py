from pathlib import Path

file_path = Path("/home/mark/Documents/Theories/raw-sources/The Simulation Hypothesis_ An MIT Computer - Rizwan Virk.txt")
text = file_path.read_text(encoding="utf-8", errors="ignore")
lines = text.splitlines()

print("Searching for 'conditional rendering' in file:")
count = 0
for i, line in enumerate(lines):
    if "conditional rendering" in line.lower() or "rendering" in line.lower():
        if "conditional" in line.lower() or "render" in line.lower():
            count += 1
            print(f"Line {i+1}: {line}")
            # print surrounding context
            for offset in range(-2, 3):
                if 0 <= i + offset < len(lines):
                    print(f"  {i+offset+1}: {lines[i+offset]}")
            print()
            if count >= 10:
                print("Truncated...")
                break
