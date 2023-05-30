#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    server = HTTPServer(('', 8080), MyHandler)
    server.serve_forever()
    
