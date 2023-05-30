#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers and returns a list of numbers. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    import random

    server = HTTPServer(("", 8080), MyHandler)
    print("Serving at port 8080")
    server.serve_forever()

<|/ file ext=.py source=github |>