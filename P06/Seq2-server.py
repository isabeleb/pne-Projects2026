import http.server
import socketserver
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        contents = ""
        n = 0
        name = ""
        seq = ""

        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)

        def read_html_file(filename):
            contents = Path("html/" + filename).read_text()
            contents = j.Template(contents)
            return contents

        sequences = ["ATTGCTGATGTAAG",
                     "TGCTGATGTCGATGT",
                     "CGTCGTGATGATGATCGT",
                     "ATCTGTCGTAGTAGT",
                     "ATGTCGTAGTGTGTATG"]

        U5 = Path("Sequences/U5_sequence.fa").read_text()
        ADA = Path("Sequences/ADA_sequence.fa").read_text()
        FRAT1 = Path("Sequences/FRAT1_sequence.fa").read_text()
        RNU6_269P = Path("Sequences/269P_sequence.fa").read_text()
        FXN = Path("Sequences/FXN_sequence.fa").read_text()

        sequences2 = {"U5": U5, "ADA": ADA, "FRAT1": FRAT1, "RNU6_269P": RNU6_269P, "FXN": FXN}

        if path == "/":
            self.send_response(200)
            contents = Path("html/index.html").read_text()

        elif path == "/ping":
            self.send_response(200)
            contents = Path("html/ping.html").read_text()

        elif path == "/get":
            self.send_response(200)
            if "n" in arguments:
                n = int(arguments["n"][0])
                if 0 <= n <= 4:
                    seq = sequences[n]
                else:
                    seq = "Invalid option"
            contents = read_html_file("get.html").render(n=n, mssg=seq)

        elif path == "/gene":
            self.send_response(200)
            if "name" in arguments:
                name = arguments["name"][0]
                if name in sequences2:
                    seq = sequences2[name].split("\n")
                    seq = seq[1:]
                    seq = "".join(seq)
                else:
                    seq = "Invalid gene"
            contents = read_html_file("gene.html").render(name=name, mssg=seq)

        elif path == "/operation":
            self.send_response(200)
            seq = arguments.get("msg", [""])[0]
            op = arguments.get("op", [""])[0].lower()
            if op == "rev":
                result = seq[::-1]
            elif op == "comp":
                bases = {"A": "T", "T": "A", "G": "C", "C": "G"}
                lst = []
                seq = seq.upper()
                for base in seq:
                    if base in bases:
                        base = bases[base]
                        lst.append(base)
                seq2 = "".join(lst)
                result = seq2
            elif op == "info":
                length = len(seq)

                def bases(base):
                    count = 0
                    for b in seq:
                        if b == base:
                            count += 1
                    return round((count / length), 2) * 100 if length > 0 else 0

                result = (
                    f"Total length: {length}\n"
                    f"A: {bases('A')}%\n "
                    f"C: {bases('C')}%\n "
                    f"G: {bases('G')}%\n "
                    f"T: {bases('T')}%\n"
                )
            else:
                result = "Invalid operator"
            contents = read_html_file("operation.html").render(mssg=seq, operation=op, info=result)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(contents.encode())))
        self.end_headers()
        self.wfile.write(contents.encode())


Handler = TestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped by the user")
        httpd.server_close()