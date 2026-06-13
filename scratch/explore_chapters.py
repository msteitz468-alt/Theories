import re
from pathlib import Path

file_path = Path("/home/mark/Documents/Theories/raw-sources/The Simulation Hypothesis_ An MIT Computer - Rizwan Virk.txt")
text = file_path.read_text(encoding="utf-8", errors="ignore")
lines = text.splitlines()

chapter_headers = [
    ("one", "Introduction to the Simulation Hypothesis"),
    ("two", "Computer Games: From Pong to MMORPGs"),
    ("three", "The Metaverse: Virtual and Augmented Realities"),
    ("four", "Mind Games and Interfaces"),
    ("five", "AI, the Singularity, and Downloadable Consciousness"),
    ("six", "The Simulation Point, Ancestor Simulations, and Beyond"),
    ("seven", "Conditional Rendering and the Collapse of the Probability Wave"),
    ("eight", "Parallel Universes, Future Selves, and Video Games"),
    ("nine", "Pixels, Quanta, and the Structure of Space-Time"),
    ("ten", "Spirits in an Illusory, Video Game–Like Dream World"),
    ("eleven", "Multiple Lives and Karma as Quests in Video Games"),
    ("twelve", "God, Angels, and the Simulation: The Western Traditions"),
    ("thirteen", "Some Unexplained Areas"),
    ("fourteen", "Skeptics and Believers: Evidence of Computation"),
    ("fifteen", "The Great Simulation and Its Implications")
]

print("Scanning for chapters in main text...")
for idx, (num_word, header) in enumerate(chapter_headers, 1):
    found = False
    for i in range(500, len(lines)):
        line = lines[i]
        # Match where line is exactly the header, or contains it with chapter number nearby
        if header in line:
            # Check if previous lines contain the chapter number word (like "one", "two")
            match_word = False
            for offset in range(1, 5):
                if i - offset >= 0 and lines[i - offset].strip().lower() == num_word:
                    match_word = True
                    break
            if match_word or line.strip() == header:
                print(f"Ch {idx} ('{header}'): found at line {i+1}")
                # print a short excerpt of 4 lines
                for j in range(1, 5):
                    if i + j < len(lines):
                        print(f"  {lines[i+j]}")
                found = True
                break
    if not found:
        # Fallback search
        for i in range(500, len(lines)):
            if header in line:
                print(f"Ch {idx} (approx): found at line {i+1}")
                break
