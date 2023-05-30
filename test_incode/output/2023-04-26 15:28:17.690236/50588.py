#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    httpd = HTTPServer(("", 80), BaseHTTPRequestHandler)
    httpd.serve_forever()
