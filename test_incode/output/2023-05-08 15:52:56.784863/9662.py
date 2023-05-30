#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that opens fruits.html and displays fruits on it.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlparse(self.path).path
            if path == "/fruits.html":
                f = open("fruits.html","r")
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(f.read())
            else:
                self.send_error(404)
    server = HTTPServer(('', 8080), MyHandler)
    server.serve_forever()

