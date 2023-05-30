#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that requests user input.
    #This example is for demonstration purposes only.
    #It is not intended for production use.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import socket
    import sys
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            length = int(self.headers['Content-Length'])
            
            body = self.rfile.read(length)
            
            self.wfile.write(body)
    
    server = HTTPServer(('', 8080), Handler)
    
    print('Serving at http://127.0.0.1:8080/')
    server.serve_forever()

