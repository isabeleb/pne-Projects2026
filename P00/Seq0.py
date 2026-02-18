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

    final_DNA_seq = DNA_seq.replace(header, "")

    print(len(final_DNA_seq))



# def seq_count_base():
# def seq_count():
# def seq_reverse():
# def seq_complement():

