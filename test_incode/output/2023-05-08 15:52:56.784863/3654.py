#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that converts a list of words.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from socketserver import ThreadingMixIn
    httpd = HTTPServer(('', 8000), MyHandler)
    httpd.serve_forever()

