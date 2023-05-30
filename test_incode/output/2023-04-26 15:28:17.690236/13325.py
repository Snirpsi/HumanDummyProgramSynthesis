#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port. """    
    
    from http.server import BaseHTTPRequestHandler
    from socketserver import ThreadingMixIn
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to a GET request. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body>')
            self.wfile.write(b'<h1>Enumerate port</h1>')
            self.wfile.write(b'</body></html>')
    
    server_address = ('', 8000)
    httpd = ThreadingMixIn(server_address, RequestHandler)
    httpd.serve_forever()
    
