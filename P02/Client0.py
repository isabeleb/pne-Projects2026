import socket
from pathlib import Path

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def ping(self):
        print("OK!")

    def __str__(self):
        return f"Connection to SERVER at {self.ip} ,PORT: {self.port}"

    def talk(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect((self.ip, self.port))

        s.send(str.encode(msg))

        response = s.recv(2048).decode("utf-8")

        s.close()

        return response



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


    def read_fasta(self, filename):
        content = Path(filename).read_text()
        content_new = content.split("\n")

        full_sequence = ("".join(content_new[1:]))

        self.strbases = full_sequence

        return full_sequence

    def __str__(self):
        return self.strbases























