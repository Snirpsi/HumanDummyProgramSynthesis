#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that opens fruits.txt and displays them.
    import os
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlparse(self.path).path
            if path == "/":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(open("fruits.txt").read())
            else:
                self.send_error(404)
    
    server = HTTPServer(('localhost', 8000), FruitHandler)
    server.serve_forever()

