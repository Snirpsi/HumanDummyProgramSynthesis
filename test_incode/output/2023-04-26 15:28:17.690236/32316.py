#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words or multiplyes a list of words. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    import random
    
    class WordsHandler(BaseHTTPRequestHandler):
        """ A simple webserver that returns words or multiplyes a list of words. """
        def do_GET(self):
            """ Respond to a GET request. """
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/':
                """ Respond to a GET request. """
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write(
                    "<html><head><title>Words</title></head><body>"
                    "<h1>Words</h1>"
                    "<p>This server responds to GET requests with words or multiplyes a list of words. "
                    "It responds to GET requests with words or multiplyes a list of words. "
                    "It responds to GET requests with words or multiplyes a list of words. "
                    "It responds to GET requests with words or multiplyes a list of words. "
                    "It responds to GET requests with words or multiplyes a list of words. "
                    "It responds to GET requests with words or multiplyes a list of words. "
                    "It responds to GET requests with words or multiplyes a list of words. "
                    "It responds to GET requests with words or multiplyes a list of words. "
                    "It responds to GET requests with words or multiplyes a list of words. "
                    "It responds to GET requests with words or multiplyes a list of words. "
                    "It responds to GET requests with words or multiplyes a list of words. "
                    "It responds to GET requests with words or multiplyes a list of words. "
                    "It responds to GET requests with words or multiplyes a list of words. "
                    "It responds to GET requests with words or multiplyes a list of words. "
                    "It responds to GET requests with words or multiplyes a list of words. "
                    "It responds to GET requests with words or multiplyes a list of words. "
                    "It responds to GET requests with words or multiplyes a list of words. "
                    "It responds to GET requests with words or multiplyes a list of words. "
                    "It responds to GET requests with words or multiplyes a list of words. "
                    "It responds to GET requests with words or multiplyes a list of words. "
                    "It responds to GET requests with words or multiplyes a list of words. "
                    "It responds to GET requests with words or multiplyes a list of words. "
                    "It responds to GET requests with words or multiplyes a list of words. "
                    "It responds to GET requests with words or multiplyes 