#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports or opens fruits. """    
    from http.server import BaseHTTPRequestHandler
    from socketserver import ThreadingMixIn
    from urllib.parse import urlparse
    from sys import argv
    from time import sleep
    from os import getenv
    from sys import exit
    
    server_address = ('', getenv('PORT'))
    httpd = BaseHTTPRequestHandler
    httpd.