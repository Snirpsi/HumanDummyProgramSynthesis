#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that opens numbers.txt and displays its contents
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import os
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type','text/plain')
            self.end_headers()
            with open('numbers.txt','r') as f:
                self.wfile.write(f.read())
    
    server = HTTPServer(('localhost', 8000), Handler)
    server.serve_forever()

