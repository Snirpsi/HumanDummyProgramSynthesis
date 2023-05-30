#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    server = HTTPServer(('', 8000), MyHandler)
    