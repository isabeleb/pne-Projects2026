from pathlib import Path

FILENAME = "sequences/U5.txt"

file_contents = Path(FILENAME).read_text()

lines_list = file_contents.split()

body_lines = lines_list[3:]

print("Body of the U5.txt file:")
for line in body_lines:
    print(line)

