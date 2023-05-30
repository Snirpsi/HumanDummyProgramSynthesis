#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that prints a list of numbers.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from socketserver import ThreadingMixIn
    from urllib.parse import urlparse
    from urllib.request import urlopen

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlparse(self.path).path
            if path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(numbers)
            else:
                self.send_error(404)

    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, Handler)
    ThreadingMixIn.instance().start()
    httpd.serve_forever()

