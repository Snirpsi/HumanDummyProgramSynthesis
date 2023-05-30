#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that opens fruits.html and displays them in browser.
    import os
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from urllib.request import urlopen

    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlparse(self.path).path
            if path == "/fruits.html":
                f = urlopen("http://127.0.0.1:8000/fruits.html")
                html = f.read()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(html)
            else:
                self.send_error(404)

    server_address = ('', 8000)
    httpd = HTTPServer(server_address, FruitHandler)
    httpd.serve_forever()

