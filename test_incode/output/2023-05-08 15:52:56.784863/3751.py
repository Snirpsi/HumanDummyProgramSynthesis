#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that prints a list of words.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from socketserver import ThreadingMixIn
    httpd = HTTPServer(('', 8000), MyHandler)
    ThreadingMixIn.instance().start()
    httpd.serve_forever()

