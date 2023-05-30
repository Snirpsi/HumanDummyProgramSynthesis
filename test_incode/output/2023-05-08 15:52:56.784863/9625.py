#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that converts fruits.txt into HTML
    import os
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from io import BytesIO
    from html import escape
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlparse(self.path).path
            if path == "/":
                f = open("fruits.txt", "r")
                content = f.read()
                f.close()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes(content, "utf8"))
            else:
                f = open(path, "r")
                content = f.read()
                f.close()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes(content, "utf8"))
    
    server = HTTPServer(('', 8000), Handler)
    server.serve_forever()

