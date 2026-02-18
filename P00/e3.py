from pathlib import Path
from Seq0 import seq_len

FOLDER = "sequences/"

FILENAMES = ["U5.txt" , "ADA.txt" , "FRAT1.txt" , "FXN.txt"]

filenames = []
for FILE in FILENAMES:
    filename = Path(FOLDER + FILE).read_text()
    filenames.append(filename)

files_dictionary = dict(zip(FILENAMES, filenames))

for F, f in files_dictionary.items():
    print("Gene:", F.replace(".txt" , "") , "-> Length:")








































