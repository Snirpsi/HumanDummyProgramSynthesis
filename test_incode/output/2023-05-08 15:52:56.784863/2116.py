#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that prints numbers.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    httpd = HTTPServer(('', 8000), BaseHTTPRequestHandler)
    httpd.serve_forever()

