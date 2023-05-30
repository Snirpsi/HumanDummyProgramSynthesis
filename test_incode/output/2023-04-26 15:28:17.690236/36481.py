#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers. """    
    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    from socketserver import ThreadingMixIn
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to GET requests. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self.