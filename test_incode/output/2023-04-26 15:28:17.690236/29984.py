#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import socketserver

    HOST, PORT = 'localhost', 8000
    Handler = BaseHTTPRequestHandler
    httpd = HTTPServer((HOST, PORT), Handler)
    httpd.serve_forever()
