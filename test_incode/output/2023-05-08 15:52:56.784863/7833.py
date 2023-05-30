#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that requests words.
    #The server will respond with "Hello, world!" when requested.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    server = HTTPServer(('', 8080), MyHandler)
    server.serve_forever()

