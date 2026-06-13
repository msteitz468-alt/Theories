with open("scratch/seth_speaks.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print("=== CHAPTER 5 (COORDINATION POINTS) START ===")
for idx in range(2968, 3120):
    if idx < len(lines):
        print(f"{idx+1}: {lines[idx]}", end="")
