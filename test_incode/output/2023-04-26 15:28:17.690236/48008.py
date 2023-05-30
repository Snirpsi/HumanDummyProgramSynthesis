#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports or opens a list of words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from socketserver import ThreadingMixIn
    
    class WordHandler(BaseHTTPRequestHandler):
        """ A simple handler for words. """
        def do_GET(self):
            """ Respond to a GET request. """
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, world!')
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, WordHandler)
    httpd.serve_forever()
    
