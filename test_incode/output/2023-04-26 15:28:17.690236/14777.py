#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from io import BytesIO
    from sys import argv
    
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    
    server_