#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes user input. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import math
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            """ Get user input. """
            
            """ Multiply user input with user input. """
            
            """ Send response back to client. """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(str(math.factorial(self.path.split('?')[1])))
            
    server = HTTPServer(("", 8080), Handler)
    server.serve_forever()
