def dna_analysis(seq):
    seq_length = len(seq)
    print("-Total length:" , seq_length)

    first_5_char =seq[0:5]
    print("-First 5 characters:", first_5_char)

    last_3_char= seq[-3:]
    print("-Last 3 characters:" , last_3_char)

    seq_to_lowercase = seq.lower()
    print("-Sequence in lowercase:" , seq_to_lowercase)

    ATC_repetition = seq.count("ATC")
    print("-ATC count:" , ATC_repetition)

    RNA_transcription = seq.replace("T" , "U")
    print("-RNA sequence:" , RNA_transcription)

dna = "ATGCGATCGATCGATCGATCGA"

dna_analysis(dna)



