#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port or opens fruits. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class FruitHandler(BaseHTTPRequestHandler):
        """ A simple handler for fruits. """
        def do_GET(self):
            """ Respond to GET requests. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(fruits.generate())
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, FruitHandler)
    
    print('Serving on port 8080...')
    httpd.serve_forever()
    
