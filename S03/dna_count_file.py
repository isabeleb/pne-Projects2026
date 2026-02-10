f = open("dna.txt" , "r")

lines = f.readlines()
f.close()

total_number = 0
total_numA = 0
total_numC = 0
total_numG = 0
total_numT = 0


for sequence in lines:
    sequence = sequence.strip()

    total_number += len(sequence)

    for base in sequence:
        if base == "A":
            total_numA += 1
        elif base == "C":
            total_numC += 1
        elif base == "G":
            total_numG += 1
        elif base == "T":
            total_numT += 1

print("Total number of bases:", total_number)
print("Total number of A:" , total_numA)
print("Total number of C:" , total_numC)
print("Total number of G:" , total_numG)
print("Total number of T:" , total_numT)





