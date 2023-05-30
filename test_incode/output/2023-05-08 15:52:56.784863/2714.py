#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that iterates over numbers.
    #It will serve the file at http://127.0.0.1:8000/numbers.txt
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import os
    import sys
    sys.path.append(os.path.abspath('..'))
    from numbers import numbers
    httpd = HTTPServer(("", 8000), NumbersHandler)
    httpd.serve_forever()

