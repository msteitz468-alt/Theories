from pathlib import Path

file_path = Path("/home/mark/Documents/Theories/raw-sources/The Simulation Hypothesis_ An MIT Computer - Rizwan Virk.txt")
text = file_path.read_text(encoding="utf-8", errors="ignore")
lines = text.splitlines()

missing = [
    "Introduction to the Simulation Hypothesis",
    "Computer Games: From Pong to MMORPGs",
    "The Metaverse: Virtual and Augmented Realities",
    "God, Angels, and the Simulation: The Western Traditions",
    "Skeptics and Believers: Evidence of Computation"
]

print("Searching for missing chapters...")
for header in missing:
    for i in range(500, len(lines)):
        if header in lines[i]:
            print(f"Header: '{header}' at line {i+1}")
            # print surrounding 5 lines
            for j in range(-2, 5):
                if 0 <= i + j < len(lines):
                    print(f"  {i+j+1}: {lines[i+j]}")
            print()
            break
