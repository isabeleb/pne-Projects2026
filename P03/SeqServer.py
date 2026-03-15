import socket
from Seq3 import Seq
import termcolor

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
            termcolor.cprint('PING command!', 'green')
            response = "OK!\n"

            print(response)

            cs.send(response.encode())


        elif "GET" in msg:
           seq_list = ["AGTGTTAGGTTAAACCCTTTAGGCGATGCTAGCTAGATATATATGGGCCCGACGCAGT",
                    "ATTTTCCCGATGCCATAGAGAGGGGTTAAGTAGAAACCCCTTTGATGCTAGGTGTGGT",
                    "TACGTGTGAAACGATCGAAGTGAAATAGATAGAAATAGATTTTAGTTTGTAGGTGGTA",
                    "GGCCCTAATCGATCGATCAGTTTAGCCCCATGCGGTCTCTAGAAATGCGTGGGATTTA",
                    "ATTAGGCCCCCCATAGATTTAGTAATATAGCTTAGCTTTCGATCGATTCCATAGGGAA"]

           n = int(msg.strip().replace("GET" , ""))

           if n not in range(len(seq_list)):
               response = "The number introduced is not valid. Please try again"
               print("Number out of range")

           else:
               termcolor.cprint('GET', 'green')

               response = seq_list[n] + "\n"

               print(response)

           cs.send(response.encode())


        elif "INFO" in msg:
            termcolor.cprint('INFO', 'green')

            sequence = msg.replace("INFO", "").strip()

            s = Seq(sequence)

            if s.strbases != "ERROR":
                seq_length = s.len()

                base_count = s.count_base()

                response1 = f"Sequence: {sequence}" + "\n"
                print(f"Sequence: {sequence}")

                response2 = f"Total length: {seq_length}" + "\n"
                print(f"Total length: {seq_length}")

                response3 = base_count + "\n"
                print(response3)

                cs.send(response1.encode())
                cs.send(response2.encode())
                cs.send(response3.encode())
            else:
                response = "Sorry, invalid sequence. Try again"
                cs.send(response.encode())

        elif "COMP" in msg:
            termcolor.cprint('COMP', 'green')

            sequence = msg.replace("COMP", "").strip()

            s = Seq(sequence)

            if s.strbases != "ERROR":
                comp_base = s.complement()

                response = comp_base + "\n"
                print(response)

                cs.send(response.encode())

            else:
                response = "Sorry, invalid sequence. Try again"
                cs.send(response.encode())


        elif "REV" in msg:
            termcolor.cprint('REV', 'green')

            sequence = msg.replace("REV", "").strip()

            s = Seq(sequence)

            if s.strbases != "ERROR":
                rev_base = s.reverse()

                response = rev_base + "\n"
                print(response)

                cs.send(response.encode())

            else:
                response = "Sorry, invalid sequence. Try again"
                cs.send(response.encode())



        elif "GENE" in msg:
            termcolor.cprint('GENE', 'green')

            gene_name = msg.replace("GENE", "").strip()

            valid_genes = ["U5" , "ADA" , "FRAT1" , "FXN" , "RNU6_269P"]

            if gene_name in valid_genes:
                filename = f"sequences/{gene_name}.txt"
                s = Seq()
                gene_seq = s.read_fasta(filename)

                response = str(gene_seq)
                print(response + "\n")

                cs.send(response.encode())

            else:
                response = "Invalid Gene Name\n"
                print(response)
                cs.send(response.encode())

        else:
            response = "Sorry, invalid command. Try again"
            cs.send(response.encode())
            print(response)


        cs.close()