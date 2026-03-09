from Client0 import Client
from Client0 import Seq

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

c_serv1 = Client("127.0.0.1", 8080)
c_serv2 = Client("127.0.0.1", 8081)

filename = "sequences/FRAT1.txt"
s = Seq()
gene_seq = s.read_fasta(filename)
gene_name = filename.replace(".txt", "").replace("sequences/", "")

start_message1 = c_serv1.talk(f"Sending the {gene_name} Gene to the server, in fragments of 10 bases...")
start_message2 = c_serv2.talk(f"Sending the {gene_name} Gene to the server, in fragments of 10 bases...")

all_fragments_dict= {"Fragment 1": gene_seq[0:10],"Fragment 2": gene_seq[20:30], "Fragment 3": gene_seq[30:40],
                     "Fragment 4": gene_seq[40:50], "Fragment 5": gene_seq[50:60],"Fragment 6": gene_seq[60:70],
                     "Fragment 7": gene_seq[70:80], "Fragment 8": gene_seq[80:90],"Fragment 9": gene_seq[90:100],
                     "Fragment 10": gene_seq[100:110]}

fragments_dict_1 = {"Fragment 1": gene_seq[0:10], "Fragment 3": gene_seq[30:40], "Fragment 5": gene_seq[50:60],
                    "Fragment 7": gene_seq[70:80], "Fragment 9": gene_seq[90:100]}

fragments_dict_2 = {"Fragment 2": gene_seq[20:30], "Fragment 4": gene_seq[40:50], "Fragment 6": gene_seq[60:70],
                    "Fragment 8": gene_seq[80:90],"Fragment 10": gene_seq[100:110]}

print(f"Gene FRAT1: {gene_seq}")
for name, fragment in all_fragments_dict.items():
    print(name+":", fragment)

print(start_message1)
for frag_name, fragment in fragments_dict_1.items():
    response = c_serv1.talk(f"{frag_name}: {fragment}")
    print(response)

print(start_message2)
for frag_name, fragment in fragments_dict_2.items():
    response = c_serv2.talk(f"{frag_name}: {fragment}")
    print(response)

