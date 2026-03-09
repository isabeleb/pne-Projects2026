from Client0 import Client
from Seq2 import Seq

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

c = Client("127.0.0.1", 8081)

genes_filenames = ["sequences/U5.txt", "sequences/FRAT1.txt", "sequences/ADA.txt"]


for filename in genes_filenames:
    s = Seq()
    gene_seq = s.read_fasta(filename)
    gene_name = filename.replace(".txt", "").replace("sequences/", "")

    start_message = c.talk(f"Sending the {gene_name} Gene to the server...")
    response = c.talk(str(s))

    print(start_message)
    print(response)




