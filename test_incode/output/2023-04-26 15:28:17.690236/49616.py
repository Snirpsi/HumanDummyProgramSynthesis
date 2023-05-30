#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words or adds user input. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlparse(self.path).path
            if path == '/':
                self.send_response(200)
                self.end_headers()
                self.wfile.write(self.server.words())
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(self.server.words())
    
    server = HTTPServer(("", 8080), Handler)
    server.serve_forever()
