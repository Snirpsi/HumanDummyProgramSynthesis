#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that requests numbers.txt and prints its contents
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import os
    import sys
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = os.path.realpath(self.path)
            filename = os.path.basename(path)
            
            if filename == 'numbers.txt':
                with open(path) as f:
                    contents = f.read()
                    self.send_response(200)
                    self.send_header('Content-type', 'text/plain')
                    self.end_headers()
                    self.wfile.write(contents)
            else:
                self.send_error(404)
    
    server = HTTPServer(('', 8000), Handler)
    server.serve_forever()

