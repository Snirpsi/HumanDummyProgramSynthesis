#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class RequestHandler(BaseHTTPRequestHandler):
        """ A simple request handler that converts numbers. """
        def do_GET(self):
            """ Convert numbers. """
            number = self.path.split('/')[-1]
            number = int(number)
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(str(number))
    
    server = HTTPServer(("", 8000), RequestHandler)
    server.serve_forever()