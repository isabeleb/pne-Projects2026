from pathlib import Path

FILENAME = "sequences/ADA.txt"

ADA_file = Path(FILENAME).read_text()

lines_list = ADA_file.split()

body_lines = lines_list[3:]

base_count = 0
for line in body_lines:
    base_count += len(line)

print("Total number of bases:" , base_count)