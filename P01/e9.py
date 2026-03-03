from Seq1 import Seq

print("-----| Practice 1, Exercise 9 |------")

FILENAME = "sequences/U5.txt"

s = Seq()

s.read_fasta(FILENAME)

print(f"Sequence : (Length: {s.len()}) {s.strbases}...")
print(f"  Bases: {s.count()}")
print(f"  Rev:   {s.reverse()}...")
print(f"  Comp:  {s.complement()}...")