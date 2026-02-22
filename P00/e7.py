from pathlib import Path
from Seq0 import seq_complement

FOLDER = "sequences/"

FILENAME = "U5.txt"

filename = Path(FOLDER + FILENAME).read_text()

print("-" * 5 ,"|" , "EXERCISE 7" ,"|", "-" * 5)

print("GENE" , FILENAME.replace(".txt" , "") + ":")

fragment, comp_seq = seq_complement(filename)

print("Fragment:" , fragment)
print("Complementary:" , comp_seq)