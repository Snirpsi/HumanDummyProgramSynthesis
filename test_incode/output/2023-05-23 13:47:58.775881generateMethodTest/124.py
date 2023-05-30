#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A minimal webserver that opens a http request.
    httpd = HTTPServer(('', 80), SimpleHTTPRequestHandler)
    httpd.serve_forever()
</code>
<|/ a tags=python,python-3.x |>
<| c |>
This doesn't seem to work. I'm getting a 502 Bad Gateway error when I try to access http://snirps.ddns.net
<|/ c |>
<| c |>
I added a working example to my answer. Try it out and let me know if it works for you.
<|/ c |>
<| c |>
This doesn't seem to work either. I'm getting a 502 Bad Gateway error when I try to access http://snirps.ddns.net
<|/ c |>
<| c |>
I added a working example to my answer. Try it out and let me know if it works for you.
<|/ c |>
<| c |>
This doesn't seem to work either. I'm getting a 502 Bad Gateway error when I try to access http://snirps.ddns.net
<|/ c |>
<| a |>
I used this code to run a python script on a remote server:
<code>
import http.server
import socketserver
import ssl
from http.server import BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(self.server.wfile.read())

class HTTPServer(BaseHTTPRequestHandler):
    def __init__(self, server_address, RequestHandlerClass):
        self.server_address = server_address
        self.RequestHandlerClass = RequestHandlerClass
        self.httpd = None
        self.socket = None
        self.server = None
        self.server_port = None

    def server_activate(self):
        self.server = socketserver.TCPServer(self.server_address, self.RequestHandlerClass)
        self.server_port = self.server.server_port
        self.server.serve_forever()

    def server_close(self):
        self.server.shutdown()
        self.server.server_close()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.server.wfile.write(self.RequestHandlerClass(post_data).handle())

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_PUT(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.server.wfile.write(self.RequestHandlerClass(post_data).handle())

    def do_DELETE(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.server.wfile.write(self.RequestHandlerClass(post_data).handle())

    def do_PATCH(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.server.wfile.write(self.RequestHandlerClass(post_data).handle())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Content-Length, Accept-Encoding, X-Requested-With')
        self.end_headers()

    def do_PATCH(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.server.wfile.write(self.RequestHandlerClass(post_data).handle())

    def do_TRACE(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.server.wfile.write(self.RequestHandlerClass(post_data).handle())

    def do_DELETE(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.server.wfile.write(self.RequestHandlerClass(post_data).handle())

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_PUT(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.server.wfile.write(self.RequestHandlerClass(post_data).handle())

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_PATCH(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.server.wfile.write(self.RequestHandlerClass(post_data).handle())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Content-Length, Accept-Encoding, X-Requested-With')
        self.end_headers()

    def do_PATCH(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.server.wfile.write(self.RequestHandlerClass(post_data).handle())

    def do_TRACE(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.server.wfile.write(self.RequestHandlerClass(post_data).handle())

    def do_DELETE(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.server.