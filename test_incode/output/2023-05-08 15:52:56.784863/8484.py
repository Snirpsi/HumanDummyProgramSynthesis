#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that requests numbers.txt and prints its contents
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import os
    import sys
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            with open('numbers.txt') as f:
                for line in f:
                    self.wfile.write(line)
    
    httpd = HTTPServer(('', 8000), Handler)
    print('Serving on port 8000...')
    httpd.serve_forever()

