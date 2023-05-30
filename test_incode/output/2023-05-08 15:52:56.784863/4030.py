#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that enumerates fruits.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from socketserver import ThreadingMixIn
    from urllib.parse import urlparse
    from os import listdir
    from os.path import isfile, join

    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlparse(self.path).path
            if path == "/":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(listdir('.')) # listdir returns filenames
            else:
                self.send_error(404)
                self.end_headers()

    class FruitThreadingMixIn(ThreadingMixIn, object):
        def serve_forever(self):
            self.server = None
            httpd = HTTPServer(('', 0), FruitHandler)
            self.server = httpd
            httpd.serve_forever()

    httpd = FruitThreadingMixIn()
    httpd.serve_forever()

