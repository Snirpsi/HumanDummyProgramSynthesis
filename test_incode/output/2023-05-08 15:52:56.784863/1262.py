#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that converts numbers.txt into HTML
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import os
    import sys
    port = int(sys.argv[1])
    httpd = HTTPServer(("", port), BaseHTTPRequestHandler)
    httpd.serve_forever()

