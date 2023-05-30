#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that converts words.txt into html and serves it.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    import os
    import sys
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlparse(self.path).path
            if path == "/":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes(open(os.path.join(os.path.dirname(__file__), "words.txt")).read().encode("utf-8"), "utf-8"))
            elif path == "/words":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes(open(os.path.join(os.path.dirname(__file__), "words.txt")).read().encode("utf-8"), "utf-8"))
            else:
                self.send_error(404)
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, Handler)
    httpd.serve_forever()

