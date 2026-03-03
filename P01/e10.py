from Seq1 import Seq

print("-----| Practice 1, Exercise 10 |------")

for a in ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]:
    s = Seq()

    s.read_fasta("sequences/" + a + ".txt")

    bases = s.count()
    m_common = 0
    base = ""

    for b in bases:
        if bases[b] > m_common:
            m_common = bases[b]
            base = b
        elif bases[b] == m_common and m_common != 0:
            base = base + " and " + b

    print(f"Gene {a}: Most frequent Base: {base} ")