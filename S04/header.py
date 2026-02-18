from pathlib import Path

FILENAME = "sequences/RNU6_269P.txt"

RNU6_269P_file = Path(FILENAME).read_text()

lines_list = RNU6_269P_file.split()

print("First line of the RNU6_269P.txt file:")
print(lines_list[0] + lines_list[1] + lines_list[2])
