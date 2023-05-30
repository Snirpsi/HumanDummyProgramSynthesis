#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    from urllib.parse import parse_qs
    
    httpd = HTTPServer(('', 8080), BaseHTTPRequestHandler)
    
    