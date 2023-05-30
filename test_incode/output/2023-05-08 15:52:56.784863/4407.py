#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that requests numbers.txt and prints them out
    from http.server import BaseHTTPRequestHandler, HTTPServer
    httpd = HTTPServer(('', 8080), BaseHTTPRequestHandler)
    httpd.serve_forever()

