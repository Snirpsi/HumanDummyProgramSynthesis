#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports and enumerates fruits. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to GET requests. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body><h1>Fruit</h1>')
            self.wfile.write(b'</body></html>')
    
    server = HTTPServer(("", 8080), FruitHandler)
    server.serve_forever()
    
