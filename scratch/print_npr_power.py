with open("scratch/nature_of_personal_reality.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print("=== CHAPTER 19 (POINT OF POWER) START ===")
for idx in range(3940, 4030):
    if idx < len(lines):
        print(f"{idx+1}: {lines[idx]}", end="")
