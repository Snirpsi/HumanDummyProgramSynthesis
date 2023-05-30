#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that iterates over fruits.
    #It also prints the current fruit name.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlparse(self.path).path
            if path == "/":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><body>")
                for fruit in fruirs:
                    self.wfile.write(b"<h1>" + fruit + "</h1>")
                self.wfile.write(b"</body></html>")
            else:
                self.send_error(404)
    server = HTTPServer(('', 8080), RequestHandler)
    server.serve_forever()

