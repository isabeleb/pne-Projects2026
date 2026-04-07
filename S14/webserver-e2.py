import http.server
import socketserver
import termcolor
from pathlib import Path

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')

        requestline_list = self.requestline.split(",")

        request = requestline_list[1]

        if request == "/" or request == "/index.html":
            file_path = Path("index.html")

        else:
            file_path = Path("error.html")


        contents = file_path.read_text()

        self.send_response(200)

        self.send_header('Content-Type', 'text/plain')
        self.send_header('Content-Length', len(contents.encode()))

        self.end_headers()


        self.wfile.write(contents.encode())

        return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()