#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports and returns fruits. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to GET requests. """
            
            fruits = []
            
            for port in range(1, 65535):
                fruits.append('http://127.0.0.1:{}/'.format(port))
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(fruits)
            
    server = HTTPServer(('', 8080), FruitHandler)
    
    print('Serving on port 8080...')
    server.serve_forever()
    
