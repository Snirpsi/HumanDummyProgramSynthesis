#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that opens numbers.txt and displays its contents
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import os
    import sys
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = os.path.abspath(self.path)
            filename = os.path.basename(path)
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            with open(path) as f:
                self.wfile.write(f.read())
    
    server = HTTPServer(('', 8000), Handler)
    server.serve_forever()

