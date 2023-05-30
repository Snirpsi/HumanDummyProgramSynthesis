#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits. """    
    
    from http.server import BaseHTTPRequestHandler
    from urllib.parse import urlparse
    import random
    
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            path = urlparse(self.path).path
            
            if path == '/fruits':
                """ Return a list of fruits. """
                
                fruits = ['apple', 'banana', 'cherry']
                
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                
                self.wfile.write(fruits[random.randint(0, len(fruits)-1)])
                
            elif path == '/fruits/<fruit>':
                """ Return a single fruit. """
                
                fruits = ['apple', 'banana', 'cherry']
                
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                
                self.wfile.write(fruits[random.randint(0, len(fruits)-1)])
                
            else:
                """ Return a 404 error. """
                
                self.send_response(404)
                self.end_headers()
                
                self.wfile.write('404 Not Found')
                
    httpd = BaseHTTPRequestHandler()
    
    httpd.