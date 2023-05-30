#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words and returns a port. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle a GET request. """
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/':
                """ Return a list of words. """
                words = ['python', 'flask', 'flask