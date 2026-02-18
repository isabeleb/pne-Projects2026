from pathlib import Path

FILENAME = "sequences/U5.txt"

U5_file = Path(FILENAME).read_text()

lines_list = U5_file.split()

body_lines = lines_list[3:]

print("Body of the U5.txt file:")
for line in body_lines:
    print(line)

