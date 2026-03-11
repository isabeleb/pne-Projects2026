import termcolor
import socket
from Seq1 import Seq

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

PORT = 8080
IP = "127.0.0.1"

ls.bind((IP, PORT))

ls.listen()

print("The server is configured!")

while True:

    print("Waiting for Clients...")

    try:
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server stopped by the user")

        ls.close()

        exit()


    else:

        msg_raw = cs.recv(2048)

        msg = msg_raw.decode()


        if msg.strip() == "PING":
            termcolor.cprint('PING COMMAND!', 'green')
            print("OK!")

            response = "OK!\n"

            cs.send(response.encode())


        elif  "GET" in msg:
           seq_list = ["AGTGTTAGGTTAAACCCTTTAGGCGATGCTAGCTAGATATATATGGGCCCGACGCAGT",
                    "ATTTTCCCGATGCCATAGAGAGGGGTTAAGTAGAAACCCCTTTGATGCTAGGTGTGGT",
                    "TACGTGTGAAACGATCGAAGTGAAATAGATAGAAATAGATTTTAGTTTGTAGGTGGTA",
                    "GGCCCTAATCGATCGATCAGTTTAGCCCCATGCGGTCTCTAGAAATGCGTGGGATTTA"]

           n = int(msg.strip().replace("GET" , ""))

           if n != 0:
               termcolor.cprint('GET', 'green')

               response = seq_list[n - 1] + "\n"

               print(response)

               cs.send(response.encode())


        elif "INFO" in msg:
            s = Seq()
            seq = msg.replace("INFO", "").strip()
            sequence = seq.__str__()

            response = s.count_base()

            cs.send(response.encode())


        cs.close()