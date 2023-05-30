#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    server = HTTPServer(('', 8080), BaseHTTPRequestHandler)
    server.serve_forever()
