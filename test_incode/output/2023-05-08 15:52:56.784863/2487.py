#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that prints a list of numbers.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from socketserver import ThreadingMixIn
    httpd = HTTPServer(('', 8000), MyHandler)
    ThreadingMixIn.instance().start()
    httpd.serve_forever()

