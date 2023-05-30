#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers or opens numbers. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class NumberHandler(BaseHTTPRequestHandler):
        """ A handler that enumerates numbers. """
        def do_GET(self):
            """ Enumerates numbers. """
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(str(enumerate([1, 2, 3, 4, 5])))
    
    server = HTTPServer(("", 8080), NumberHandler)
    server.serve_forever()
    
