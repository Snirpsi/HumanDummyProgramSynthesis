#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that adds words.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    server = HTTPServer(('', 8000), BaseHTTPRequestHandler)
    server.serve_forever()

