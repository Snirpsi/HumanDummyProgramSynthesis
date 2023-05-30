#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that opens numbers.txt and prints its contents
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import os
    import sys
    httpd = HTTPServer(("", 80), MyHandler)
    httpd.serve_forever()

