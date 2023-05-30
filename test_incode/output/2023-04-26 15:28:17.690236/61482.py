#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    httpd = HTTPServer(('localhost', 8080), MyHandler)
    httpd.serve_forever()
    
