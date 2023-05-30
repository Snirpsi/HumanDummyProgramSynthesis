#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that opens fruits.html and displays them in browser.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    import os
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlparse(self.path).path
            if path == "/fruits.html":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(fruirs)
            else:
                self.send_error(404)
    
    server_address = ('localhost', 8080)
    httpd = HTTPServer(server_address, Handler)
    httpd.serve_forever()

