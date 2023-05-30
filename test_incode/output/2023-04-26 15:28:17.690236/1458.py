#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers. """    
    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    server = HTTPServer(('localhost', 8080), BaseHTTPRequestHandler)
    server.serve_forever()
    
