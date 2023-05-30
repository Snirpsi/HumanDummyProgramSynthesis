#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that converts numbers.txt into HTML
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import os
    import sys
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes('<html><body>', 'utf-8'))
            self.wfile.write(bytes('<body><h1>', 'utf-8'))
            self.wfile.write(bytes('Numbers Listing!', 'utf-8'))
            self.wfile.write(bytes('</body></html>', 'utf-8'))
    
    httpd = HTTPServer(("", 8000), Handler)
    httpd.serve_forever()

