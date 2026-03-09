from Client0 import Client
from Client0 import Seq

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

c = Client("127.0.0.1", 8081)

filename = "sequences/FRAT1.txt"
s = Seq()
gene_seq = s.read_fasta(filename)
gene_name = filename.replace(".txt", "").replace("sequences/", "")
start_message = c.talk(f"Sending the {gene_name} Gene to the server, in fragments of 10 bases...")

F1 = gene_seq[0:10]
F2 = gene_seq[10:20]
F3 = gene_seq[20:30]
F4 = gene_seq[30:40]
F5 = gene_seq[40:50]

fragments_dict = {"Fragment 1" : F1, "Fragment 2" : F2, "Fragment 3": F3, "Fragment 4" :F4, "Fragment 5": F5}
print(start_message)
print(f"Gene FRAT1: {gene_seq}")
for name, fragment in fragments_dict.items():
    print(name, fragment)

for frag_name, fragment in fragments_dict.items():
    response = c.talk(f"{frag_name}: {fragment}")
    print(response)


