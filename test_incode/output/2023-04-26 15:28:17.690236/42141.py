#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    server = HTTPServer(('', 80), BaseHTTPRequestHandler)
    server.