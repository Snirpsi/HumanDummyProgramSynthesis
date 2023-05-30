#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port. """    
    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    server = HTTPServer(('localhost', 8000), BaseHTTPRequestHandler)
    server.serve_forever()
    
