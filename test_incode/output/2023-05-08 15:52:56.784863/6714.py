#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that iterates over user input.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    import socket
    
    HOST, PORT = 'localhost', 8080
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlparse(self.path).path
            if path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<h1>Hello World!</h1>')
            else:
                self.send_error(404)
    
    httpd = HTTPServer(('', PORT), Handler)
    print('Serving on port {}'.format(PORT))
    httpd.serve_forever()

