class NumberGuesser:

    def __init__(self, secret_number, attempts):
        self.secret_number = secret_number
        self.attempts = attempts

        if secret_number not in range(1,101):
            self.secret_number = "Invalid"
            print("The number must be between 1 and 100")
        else:
            self.secret_number = input("Enter the number to guess:")


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
        return  f" A: {b_count['A']},   C: {b_count['C']},   G: {b_count['G']},   T: {b_count['T']}"


    def count(self):
        b_count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        if self.strbases not in ["NULL", "ERROR"]:
            for b in self.strbases:
                if b in b_count:
                    b_count[b] += 1
        return b_count





