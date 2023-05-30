#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that converts numbers.txt into HTML
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import os
    import sys
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = os.path.join(self.path, os.path.basename(self.path))
            
            if os.path.isfile(path):
                with open(path) as file:
                    content = file.read()
                    
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(content)
            else:
                self.send_error(404)
    
    server = HTTPServer(('', 8000), Handler)
    
    server.serve_forever()

