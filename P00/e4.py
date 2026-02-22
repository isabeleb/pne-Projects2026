from pathlib import Path
from Seq0 import seq_count_base

FOLDER = "sequences/"

FILENAMES = ["U5.txt" , "ADA.txt" , "FRAT1.txt" , "FXN.txt"]

filenames = []
for FILE in FILENAMES:
    filename = Path(FOLDER + FILE).read_text()
    filenames.append(filename)

files_dictionary = dict(zip(FILENAMES, filenames))

print("-" * 5 ,"|" , "EXERCISE 4" ,"|", "-" * 5)

for F, f in files_dictionary.items():
    count_A, count_C, count_G, count_T = seq_count_base(f)
    print("\n")
    print("Gene" , F.replace(".txt" , "") + ":")
    print("A:" , count_A)
    print("C:", count_C)
    print("G:", count_G)
    print("T:", count_T)











