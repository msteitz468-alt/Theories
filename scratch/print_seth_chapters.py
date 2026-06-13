with open("scratch/seth_speaks.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print("=== CHAPTER 5 (COORDINATION POINTS) START ===")
for idx in range(2968, 3050):
    if idx < len(lines):
        print(f"{idx+1}: {lines[idx]}", end="")

print("\n=== CHAPTER 21 (THREE CHRISTS) START ===")
for idx in range(13480, 13650):
    if idx < len(lines):
        print(f"{idx+1}: {lines[idx]}", end="")
