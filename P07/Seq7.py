from pathlib import Path

class Seq:

    def __init__(self, strbases=None):
        self.strbases = strbases
        base_list = ["A", "C", "G", "T"]

        if strbases == None:
            self.strbases = "NULL"
            print("NULL sequence created")
        else:
            for element in strbases:
                if element not in base_list:
                    self.strbases = "ERROR"

            if self.strbases == "ERROR":
                print("INVALID sequence!")
            else:
                print("New sequence created!")

    def __str__(self):
        return self.strbases


    def len(self):
        if self.strbases == "ERROR":
            length = 0
        elif self.strbases == "NULL":
            length = 0
        else:
            length = len(self.strbases)
        return length


    def count_base(self):
        b_count = {"A": 0, "C": 0, "G": 0, "T": 0}
        if self.strbases not in ["NULL", "ERROR"]:
           for base in self.strbases:
               if base in b_count:
                b_count[base] += 1
        return  b_count


    def count(self):
        b_count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        if self.strbases not in ["NULL", "ERROR"]:
            for b in self.strbases:
                if b in b_count:
                    b_count[b] += 1
        return b_count


    def reverse(self):
        base_list = []
        if self.strbases == "NULL":
            new_seq = self.strbases
        elif self.strbases == "ERROR":
            new_seq = self.strbases
        else:
            rev_seq = self.strbases[::-1]
            for base in rev_seq:
                base_list.append(base)
            new_seq = ''.join(base_list)
        return new_seq


    def complement(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return self.strbases
        new_seq = ""
        for b in self.strbases:
            base = b.upper()
            if base == "A":
                new_seq += "T"
            elif base == "T":
                new_seq += "A"
            elif base == "C":
                new_seq += "G"
            elif base == "G":
                new_seq += "C"

        return new_seq


    def read_fasta(self, filename):
        content = Path(filename).read_text()
        content_new = content.split("\n")

        full_sequence = ("".join(content_new[1:]))

        self.strbases = full_sequence
