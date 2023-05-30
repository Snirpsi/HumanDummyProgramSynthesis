#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(fruits)
    
    server = HTTPServer(('', 8080), FruitHandler)
    server.serve_forever()
    
