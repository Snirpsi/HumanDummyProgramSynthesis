#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that opens fruits.html and displays fruits
    #on localhost:8000
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    import os
    import sys
    
    
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlparse(self.path).path
            if path == "/fruits.html":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(open("fruits.html").read())
            else:
                self.send_error(404)
    
    
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, FruitHandler)
    httpd.serve_forever()

