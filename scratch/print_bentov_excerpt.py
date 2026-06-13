with open("scratch/stalking_the_wild_pendulum.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
print("=== Lines 175-230 ===")
for i in range(174, min(len(lines), 230)):
    print(f"{i+1}: {lines[i]}", end="")
