#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits or opens a port. """    
    from http.server import BaseHTTPRequestHandler
    from urllib.parse import urlparse
    
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Return a list of fruits. """
            
            path = urlparse(self.path).path
            
            if path == '/fruits':
                """ Return a list of fruits. """
                
                fruits = ['apple', 'orange', 'banana', 'cherry']
                
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(fruits)
            else:
                """ Return a list of fruits. """
                
                fruits = ['apple', 'orange', 'banana', 'cherry']
                
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(fruits)
    
    server_address = ('', 8080)
    httpd = BaseHTTPServer.HTTPServer(server_address, FruitHandler)
    httpd.serve_forever()
    
