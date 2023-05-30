#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from socketserver import ThreadingMixIn
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            # Get the port from the query string.
            port = self.path.split('=')[1]
            
            # Open a socket to the port and receive the data.
            self.wfile.write(self.request