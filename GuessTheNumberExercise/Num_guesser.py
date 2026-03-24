class NumberGuesser:

    def __init__(self, secret_number, attempts=None):
        self.secret_number = secret_number
        self.attempts = attempts


    def guess(self, number):
        if number < self.secret_number:
            string = "Higher"
            self.attempts += 1
        elif number > self.secret_number:
            string = "Lower"
            self.attempts += 1
        else:
            string = f"CONGRATS! You won after {self.attempts} attempts"

        return string









