import socket

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

PORT = 8080
IP = "212.128.255.65"

ls.bind((IP, PORT))

ls.listen()

print("The server is configured!")

while True:

    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server stopped by the user")

        ls.close()

        exit()


    else:

        print(f"CONNECTION 1. Client IP, PORT: {IP}, {PORT}")

        msg_raw = cs.recv(2048)

        msg = msg_raw.decode()

        print(f"Message received: {msg}")

        response = F"ECHO: {msg}"

        cs.send(response.encode())

        cs.close()