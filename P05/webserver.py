import http.server
import socketserver
import termcolor
from pathlib import Path

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):


    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')

        request = self.requestline.strip("GET").strip("HTTP/1.1").strip(" ")

        req_file = request.strip("/")

        try:
            if request == "/":
                req_file = "index.html"

                if req_file == "index.html":
                    file_path = Path("html/" + req_file)

                else:
                    file_path = Path("html/info/" + req_file)

            self.send_response(200)


        except FileNotFoundError:
            file_path = Path("html/" + "error.html")
            self.send_response(404)

        contents = file_path.read_text()

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        self.end_headers()


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()