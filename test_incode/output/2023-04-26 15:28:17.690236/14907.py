#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port or enumerates fruits. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import socket
    
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            fruits = socket.getaddrinfo('localhost', 80)[0][-1]
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(fruits)
    
    server = HTTPServer(('', 80), FruitHandler)
    
    print('Serving on port 80')
    server.serve_forever()

<|/ file source=github ext=.py |>