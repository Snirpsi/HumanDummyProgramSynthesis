#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Serve the fruits. """
            
            path = urlparse(self.path).path
            
            if path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(fruits)
            else:
                self.send_error(404)
    
    server = HTTPServer(("", 80), FruitHandler)
    server.serve_forever()
    
