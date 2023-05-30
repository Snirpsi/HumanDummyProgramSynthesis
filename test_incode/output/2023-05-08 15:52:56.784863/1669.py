#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that adds words.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    httpd = HTTPServer(('localhost', 8000), BaseHTTPRequestHandler)
    httpd.serve_forever()

