#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from socketserver import ThreadingMixIn
    
    class WordHandler(BaseHTTPRequestHandler):
        """ A simple HTTP request handler that responds to GET requests. """
        def do_GET(self):
            """ Respond to GET requests. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self.server.words[int(self.path[1:])])
    
    server_address = ('localhost', 8080)
    httpd = HTTPServer(server_address, WordHandler)
    
    ThreadingMixIn.