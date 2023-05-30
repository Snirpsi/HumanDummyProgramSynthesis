#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    server = HTTPServer(('localhost', 8080), BaseHTTPRequestHandler)
    server.serve_forever()
