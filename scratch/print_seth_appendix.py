with open("scratch/seth_speaks.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print("=== APPENDIX (COORDINATION POINTS) START ===")
for idx in range(15600, 15720):
    if idx < len(lines):
        print(f"{idx+1}: {lines[idx]}", end="")
