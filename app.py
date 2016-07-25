import http.server

PORT = 8080 

class handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200, "OK")
        self.send_header("Content-type", "text")
        self.end_headers()
        self.flush_headers()
        self.wfile.write(b"hello")


def run(server_class=http.server.HTTPServer,
        handler_class=handler):
    print("serving at port {}".format(PORT))
    server_address = ("", PORT)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == '__main__':
    run()