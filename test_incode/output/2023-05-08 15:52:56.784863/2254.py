#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that iterates over words.
    #It will serve the words in reverse order.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    server = HTTPServer(("", 8000), MyHandler)
    server.serve_forever()

