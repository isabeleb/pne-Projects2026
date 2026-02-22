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
    lines_list = seq.split()
    header = (lines_list[0] + lines_list[1] + lines_list[2])
    DNA_seq = "".join(lines_list)
    DNA_seq_wo_header = DNA_seq.replace(header, "")

    final_DNA_seq = DNA_seq_wo_header.strip()

    fragment = final_DNA_seq[:n]

    reverse_seq = fragment[::-1]

    return fragment, reverse_seq


def seq_complement(seq):
    lines_list = seq.split()
    header = (lines_list[0] + lines_list[1] + lines_list[2])
    DNA_seq = "".join(lines_list)
    DNA_seq_wo_header = DNA_seq.replace(header, "")

    final_DNA_seq = DNA_seq_wo_header.strip()

    fragment = final_DNA_seq[:20]

    complementary_fragment = fragment.replace("A","t").replace("T" , "a").replace("C", "g").replace("G" , "c")

    return fragment, complementary_fragment.upper()


def most_common_base(seq):
    lines_list = seq.split()
    header = (lines_list[0] + lines_list[1] + lines_list[2])
    DNA_seq = "".join(lines_list)
    DNA_seq_wo_header = DNA_seq.replace(header, "")

    final_DNA_seq = DNA_seq_wo_header.strip()

    count_A = final_DNA_seq.count("A")
    count_C = final_DNA_seq.count("C")
    count_G = final_DNA_seq.count("G")
    count_T = final_DNA_seq.count("T")

    m_common_base_count = count_A
    m_common_base = "A"

    if count_C > m_common_base_count:
        m_common_base_count = count_C
        m_common_base = "C"

    if count_G > m_common_base_count:
        m_common_base_count = count_G
        m_common_base = "G"

    if count_T > m_common_base_count:
        m_common_base_count = count_T
        m_common_base = "T"

    return m_common_base





