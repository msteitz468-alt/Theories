with open("scratch/stalking_the_wild_pendulum.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print("File markers found:")
for idx, line in enumerate(lines):
    if "=== FILE:" in line:
        print(f"Line {idx+1}: {line.strip()}")
