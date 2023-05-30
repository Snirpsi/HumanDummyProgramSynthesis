#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that enumerates a list of words.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from socketserver import ThreadingMixIn
    from urllib.parse import urlparse

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed = self.path.split('?')
            path = parsed[0]
            words = parsed[1]
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(words)

    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, Handler)
    ThreadingMixIn.instance().start()
    httpd.serve_forever()

