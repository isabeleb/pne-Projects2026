#LIBRARY OF FUNCTIONS:

def seq_ping():
    print("OK")


def seq_read_fasta(filename):

    lines_list = filename.split()

    header = (lines_list[0] + lines_list[1] + lines_list[2])

    DNA_seq = "".join(lines_list)

    final_DNA_seq = DNA_seq.replace(header, "")

    print("The first 20 bases are:" , final_DNA_seq[:20])


def seq_len(seq):
    lines_list = seq.split()

    header = (lines_list[0] + lines_list[1] + lines_list[2])

    DNA_seq = "".join(lines_list)

    DNA_seq_wo_header = DNA_seq.replace(header, "")

    final_DNA_seq = DNA_seq_wo_header.strip()

    return len(final_DNA_seq)


def seq_count_base(seq):
    lines_list = seq.split()

    header = (lines_list[0] + lines_list[1] + lines_list[2])

    DNA_seq = "".join(lines_list)

    DNA_seq_wo_header = DNA_seq.replace(header, "")

    final_DNA_seq = DNA_seq_wo_header.strip()

    count_A = final_DNA_seq.count("A")
    count_C = final_DNA_seq.count("C")
    count_G = final_DNA_seq.count("G")
    count_T = final_DNA_seq.count("T")

    return count_A, count_C, count_G, count_T


def seq_count(seq):
    lines_list = seq.split()

    header = (lines_list[0] + lines_list[1] + lines_list[2])

    DNA_seq = "".join(lines_list)

    DNA_seq_wo_header = DNA_seq.replace(header, "")

    final_DNA_seq = DNA_seq_wo_header.strip()

    count_A = final_DNA_seq.count("A")
    count_C = final_DNA_seq.count("C")
    count_G = final_DNA_seq.count("G")
    count_T = final_DNA_seq.count("T")

    return dict(A = count_A , C = count_C , G = count_G , T = count_T )


def seq_reverse(seq, n):
    n = 20
# def seq_complement():

