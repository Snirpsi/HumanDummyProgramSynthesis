#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            """ Get the fruit. """
            fruit = self.path[1:]
            
            """ Convert the fruit. """
            fruit = self.convert(fruit)
            
            """ Send the converted fruit. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(fruit)
    
    server = HTTPServer(('', 8000), Handler)
    server.serve_forever()
    
