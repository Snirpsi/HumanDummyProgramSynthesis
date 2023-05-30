#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that adds user input.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from socketserver import ThreadingMixIn

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlparse(self.path).path
            if path == '/':
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'Hello World!')
            else:
                self.send_error(404, path)

    server_address = ('', 8080)
    httpd = HTTPServer(server_address, Handler)
    ThreadingMixIn.instance().start()
    httpd.serve_forever()

