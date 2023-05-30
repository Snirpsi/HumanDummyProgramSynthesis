#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words or converts a list of numbers. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs
    import random

    class WordsHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to a GET request """
            words = parse_qs(urlparse(self.path).query)
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            self.wfile.write(b'\n'.join(words))
            
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, WordsHandler)
    httpd.serve_forever()
    
