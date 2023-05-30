#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that converts words.txt into html
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlparse(self.path).path
            if path == "/":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes(open("words.txt").read(),"utf-8"))
            else:
                self.send_error(404)
    httpd = HTTPServer(('', 80), Handler)
    httpd.serve_forever()

