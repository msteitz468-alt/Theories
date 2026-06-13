with open("scratch/stalking_the_wild_pendulum.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

markers = [
    (122, "Preface"),
    (143, "Intro"),
    (180, "Chapter 1"),
    (286, "Chapter 2"),
    (346, "Chapter 3"),
    (409, "Chapter 4"),
    (506, "Chapter 5"),
    (578, "Chapter 6"),
    (690, "Chapter 7"),
    (736, "Chapter 8"),
    (811, "Chapter 9"),
    (872, "Chapter 10"),
    (922, "Epilog"),
    (934, "Appendix")
]

for line_num, name in markers:
    print(f"=== {name} (Line {line_num}) ===")
    # Print the line after the marker and next 2 non-empty lines
    idx = line_num
    printed = 0
    while idx < len(lines) and printed < 3:
        line = lines[idx].strip()
        if line:
            print(f"  {line[:200]}")
            printed += 1
        idx += 1
    print("-" * 50)
