#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from socketserver import ThreadingMixIn
    from 