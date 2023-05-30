#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that enumerates fruits.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlparse(self.path).path
            if path == "/":
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"Hello, world!")
            else:
                self.send_error(404, b"Not found")
    
    server = HTTPServer(('', 8080), Handler)
    server.serve_forever()

