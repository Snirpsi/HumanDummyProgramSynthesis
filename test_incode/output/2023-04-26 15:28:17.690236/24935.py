#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port. """    
    
    from http.server import BaseHTTPRequestHandler
    from socketserver import ThreadingMixIn
    
    class Handler(BaseHTTPRequestHandler):
        """ A simple http server that opens a port. """
        
        def do_GET(self):
            """ Handle a GET request. """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(self.