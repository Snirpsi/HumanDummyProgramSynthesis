#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports and returns fruits. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    server = HTTPServer(('', 0), BaseHTTPRequestHandler)
    server.serve_forever()
    
