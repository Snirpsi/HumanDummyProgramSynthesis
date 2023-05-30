#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import random
    import math
    
    class WordsHandler(BaseHTTPRequestHandler):
        """ A simple HTTP handler that returns a list of words. """
        def do_GET(self):
            """ Respond to a GET request by sending a list of words. """
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(
                ' '.join(random.sample(
                    ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'),
                    random.randint(1, 20))
                )
            )
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, WordsHandler)
    print('Starting server...')
    httpd.serve_forever()

<|/ file source=github ext=.py |>