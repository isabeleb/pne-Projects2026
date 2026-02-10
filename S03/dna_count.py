def count_bases(seq):
    count_A = 0
    count_C = 0
    count_G = 0
    count_T = 0
    for base in seq:
        if base == "A":
            count_A += 1
        elif base == "C":
            count_C += 1
        elif base == "G":
            count_G += 1
        elif base == "T":
            count_T += 1
    return count_A, count_C, count_G, count_T

DNA_seq = (input("Enter a DNA sequence:")).upper()

(count_A, count_C, count_G, count_T) = count_bases(DNA_seq)

print("Length of the sequence:" , len(DNA_seq))
print("A:", count_A)
print("C:", count_C)
print("G:", count_G)
print("T:", count_T)




