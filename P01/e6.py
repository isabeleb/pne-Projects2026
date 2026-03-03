from Seq1 import Seq

print("-----| Practice 1, Exercise 6 |------")

s0 = Seq()
s1 = Seq("ACTGA")
s2 = Seq("Invalid sequence")

print(f"Sequence 1: (Length: {s0.len()}) {s0}\n  Bases: {s0.count()}")
print(f"Sequence 2: (Length: {s1.len()}) {s1}\n  Bases: {s1.count()}")
print(f"Sequence 3: (Length: {s2.len()}) {s2}\n  Bases: {s2.count()}")