#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that requests numbers.
    #It will then print them out to the terminal.
    import sys
    from http.server import BaseHTTPRequestHandler,HTTPServer
    httpd = HTTPServer(('',80),MyHandler)
    httpd.serve_forever()

