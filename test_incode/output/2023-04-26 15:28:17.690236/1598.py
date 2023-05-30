#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port. """    
    from http.server import BaseHTTPRequestHandler
    from socketserver import ThreadingMixIn
    from urllib.parse import urlparse
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=8000, help='port to listen on')
    args = parser.parse_args()
    
    httpd = BaseHTTPRequestHandler
    httpd.