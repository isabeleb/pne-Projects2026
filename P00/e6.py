from pathlib import Path
from Seq0 import seq_reverse


FOLDER = "sequences/"

FILENAME = "U5.txt"

filename = Path(FOLDER + FILENAME).read_text()

print("-" * 5 ,"|" , "EXERCISE 6" ,"|", "-" * 5)

print("GENE" , FILENAME.replace(".txt" , ""))

rev_seq, fragment = seq_reverse(filename, 20)

print("Fragment:" , fragment)
print("Reverse:" , rev_seq)

