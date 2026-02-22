from pathlib import Path
from Seq0 import seq_read_fasta

FOLDER = "sequences/"

FILENAME = "U5.txt"

filename = Path(FOLDER + FILENAME).read_text()

print("-" * 5 ,"|" , "EXERCISE 2" ,"|", "-" * 5)

print("DNA FILE:" , FILENAME)

seq_read_fasta(filename)


