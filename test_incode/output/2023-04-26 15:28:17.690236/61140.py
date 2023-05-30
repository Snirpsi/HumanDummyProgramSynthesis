#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words. """    
    import sys
    from http.server import BaseHTTPRequestHandler
    from urllib.parse import urlparse
    from urllib.request import urlopen
    from io import BytesIO

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle a GET request. """
            path = self.path.rstrip('/')
            words = urlopen(path).read().splitlines()
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'\n'.join(words))

    server_address = ('localhost', 8000)
    httpd = BaseHTTPRequestHandler.HTTPServer(server_address, Handler)
    httpd.serve_forever()

