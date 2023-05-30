#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that converts numbers.txt into html and prints it.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import cgi
    import os
    import sys
    
    httpd = HTTPServer(("", 80), MyHandler)
    print("Serving at port 80")
    httpd.serve_forever()

