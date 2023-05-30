#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers or converts a list of words. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import socketserver

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes('<html><body><h1>Enumerate</h1></body></html>', 'UTF-8'))

    server = HTTPServer(("", 8000), Handler)
    server.serve_forever()
