#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    httpd = HTTPServer(('', 0), MyHandler)
    
    httpd.serve_forever()
    
