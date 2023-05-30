#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that removes fruits.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlparse(self.path).path
            if path == "/":
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes(
                    "<html><head><title>Remove Fruits</title></head>"
                    "<body><p>Remove fruits:</p></body></html>",
                    "utf8"))
            elif path == "/remove":
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes(
                    "<html><head><title>Remove Fruits</title></head>"
                    "<body><p>Remove fruits:</p></body></html>",
                    "utf8"))
            else:
                self.send_error(404)
                self.end_headers()
                return
    server = HTTPServer(('', 8080), MyHandler)
    server.serve_forever()

