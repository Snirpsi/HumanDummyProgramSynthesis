#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that removes user input.
    #It also serves up static files if requested.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import os
    import sys
    
    httpd = HTTPServer(("", 80), BaseHTTPRequestHandler)
    httpd.serve_forever()

