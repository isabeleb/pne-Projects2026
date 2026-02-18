from pathlib import Path

FILENAME = "sequences/ADA.txt"

file_contents = Path(FILENAME).read_text()

lines_list = file_contents.split()

body_lines = lines_list[3:]

base_count = 0
for line in body_lines:
    base_count += len(line)

print("Total number of bases:" , base_count)