#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits and returns words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    
    class FruitHandler(BaseHTTPRequestHandler):
        """ A handler for requests to fruits.