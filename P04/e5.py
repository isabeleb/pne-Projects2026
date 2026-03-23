import socket
from pathlib import Path
import termcolor


IP = "127.0.0.1"
PORT = 8080


def process_client(s):
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")

    lines = req.split('\n')

    req_line = lines[0]

    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")

    req_line_strip  = req_line.split(" ")

    requested_file = req_line_strip[1]

    implemented_resources = ["/info/A", "/info/C", "/info/G", "/info/T"]

    if "favicon.ico" in requested_file:
        return

    elif requested_file in implemented_resources:
        file_path = Path("html/"+requested_file+".html")

    else:
        file_path = Path("html/error.html")

    body = file_path.read_text()

    status_line = "HTTP/1.1 200 OK\n"


    header = "Content-Type: text/html\n"


    header += f"Content-Length: {len(body)}\n"


    response_msg = status_line + header + "\n" + body
    cs.send(response_msg.encode())


ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))

ls.listen()

print("Green server configured!")

while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped!")
        ls.close()
        exit()
    else:

        process_client(cs)

        cs.close()