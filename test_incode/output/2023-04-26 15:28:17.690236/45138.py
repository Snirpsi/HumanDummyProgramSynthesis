#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Return a list of fruits. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            fruits = ['apple', 'banana', 'cherry']
            self.wfile.write(fruits)
            self.wfile.close()
    
    server = HTTPServer(('', 8080), FruitHandler)
    server.serve_forever()

<|/ file source=github |>