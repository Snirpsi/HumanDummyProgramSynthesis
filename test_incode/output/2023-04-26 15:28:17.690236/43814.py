#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs
    import math

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ GET request to /. """
            query = parse_qs(