from pathlib import Path

FILENAME = "sequences/RNU6_269P.txt"

file_contents = Path(FILENAME).read_text()

lines_list = file_contents.split()

print("First line of the RNU6_269P.txt file:")
print(lines_list[0] + lines_list[1] + lines_list[2])
