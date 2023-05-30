#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body><h1>All ports open</h1></body></html>')
    
    server = HTTPServer(("", 8080), Handler)
    server.serve_forever()
    
