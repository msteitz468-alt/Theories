import re

with open("scratch/seth_speaks.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

chapters = [
    "I DO NOT HAVE A PHYSICAL BODY",
    "MY PRESENT ENVIRONMENT",
    "MY WORK AND THOSE DIMENSIONS",
    "REINCARNATIONAL DRAMAS",
    "HOW THOUGHTS FORM MATTER",
    "THE SOUL AND THE NATURE",
    "THE POTENTIALS OF THE SOUL",
    "SLEEP, DREAMS, AND CONSCIOUSNESS",
    "THE “DEATH” EXPERIENCE",
    "“DEATH” CONDITIONS IN LIFE",
    "AFTER-DEATH CHOICES AND",
    "REINCARNATIONAL RELATIONSHIPS",
    "REINCARNATION, DREAMS, AND THE HIDDEN MALE",
    "STORIES OF THE BEGINNING",
    "REINCARNATIONAL CIVILIZATIONS",
    "PROBABLE SYSTEMS, MEN, AND GODS",
    "PROBABILITIES, THE NATURE OF GOOD AND EVIL",
    "VARIOUS STAGES OF CONSCIOUSNESS",
    "ALTERNATE PRESENTS AND MULTIPLE FOCUS",
    "QUESTIONS AND ANSWERS",
    "THE MEANING OF RELIGION",
    "A GOODBYE AND AN INTRODUCTION",
    "APPENDIX"
]

print("Scanning for chapters:")
for idx, ch in enumerate(chapters):
    found = False
    for line_num, line in enumerate(lines):
        # Match only uppercase chapter headers in context
        if ch in line.upper() and ("CHAPTER" in lines[max(0, line_num-5):line_num+5] or "APPENDIX" in line.upper()):
            # Make sure it's not the Table of Contents (line_num > 200)
            if line_num > 250:
                print(f"Ch {idx+1} ({ch}): line {line_num+1}")
                found = True
                break
    if not found:
        # Broad search
        for line_num, line in enumerate(lines):
            if ch in line.upper() and line_num > 250:
                print(f"Ch {idx+1} (broad) ({ch}): line {line_num+1}")
                found = True
                break
