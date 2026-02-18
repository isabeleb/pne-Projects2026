from pathlib import Path

FOLDER = "sequences/"

FILENAME = "U5.txt"

filename = Path(FOLDER + FILENAME).read_text()

print("DNA FILE:" , FILENAME)

from Seq0 import seq_read_fasta

seq_read_fasta(filename)


