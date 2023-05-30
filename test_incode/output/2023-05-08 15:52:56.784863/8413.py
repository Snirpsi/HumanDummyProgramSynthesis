#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that removes words.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from socketserver import ThreadingMixIn
    server = HTTPServer(('', 8000), MyHandler)
    ThreadingMixIn.instance().start()
    server.serve_forever()

