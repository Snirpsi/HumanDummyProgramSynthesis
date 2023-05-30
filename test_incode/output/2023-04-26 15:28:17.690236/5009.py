#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs
    import random
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ GET request. """
            query = parse_qs(