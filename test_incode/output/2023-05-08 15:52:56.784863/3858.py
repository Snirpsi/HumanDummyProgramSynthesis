#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that prints words.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    server = HTTPServer(('localhost', 8000), BaseHTTPRequestHandler)
    server.serve_forever()

