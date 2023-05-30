#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that adds a list of words.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from socketserver import ThreadingMixIn
    from urllib.parse import urlparse
    from io import BytesIO

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            path = parsed_url.path
            if path == "/":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(BytesIO(words).read())
            else:
                self.send_error(404)
                self.end_headers()

    server = HTTPServer(('', 8080), Handler)
    ThreadingMixIn.instance().start()
    server.serve_forever()

