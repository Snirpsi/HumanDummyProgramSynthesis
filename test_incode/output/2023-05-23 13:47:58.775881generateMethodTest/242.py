#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A minimal webserver that returns a http request.
    server = HTTPServer((url, 80), RequestHandler)
    server.serve_forever()
</code>
<|/ a tags=python,python-3.x |>
<| c |>
This doesn't seem to work for me. I'm getting a 404 error when I try to access `http://snirps.ddns.net`
<|/ c |>
<| c |>
I added a working example to my answer. Try it out and let me know if it works for you.
<|/ c |>
<| c |>
I added a working example to my answer. Try it out and let me know if it works for you.
<|/ c |>
<| c |>
This doesn't seem to work for me. I'm getting a 404 error when I try to access `http://snirps.ddns.net`
<|/ c |>
<| c |>
I added a working example to my answer. Try it out and let me know if it works for you.
<|/ c |>
<| a dscore=2 |>
The code below is based on a tutorial I found online. It works fine for me and you can see it working here: https://gist.github.com/jamesrobinson/f094edb70e3ca7d74e
<code>
import http.server
import socketserver

PORT = 80

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(self.server.url_root)

class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    allow_reuse_address = True

class ThreadedHTTPRequestServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    allow_reuse_address = True

if __name__ == '__main__':
    server_address = ('', PORT)
    httpd = ThreadedHTTPServer(server_address, RequestHandler)
    httpd.serve_forever()
</code>
<|/ a tags=python,python-3.x |>
<| c |>
This doesn't seem to work for me. I'm getting a 404 error when I try to access `http://snirps.ddns.net`
<|/ c |>
<| c |>
I added a working example to my answer. Try it out and let me know if it works for you.
<|/ c |>
<| c |>
This doesn't seem to work for me. I'm getting a 404 error when I try to access `http://snirps.ddns.net`
<|/ c |>
<| c |>
I added a working example to my answer. Try it out and let me know if it works for you.
<|/ c |>
<| a dscore=2 |>
I used the code from https://gist.github.com/jamesrobinson/f094edb70e3ca7d74e
<code>
import http.server
import socketserver

PORT = 80

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(self.server.url_root)

class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    allow_reuse_address = True

class ThreadedHTTPRequestServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    allow_reuse_address = True

if __name__ == '__main__':
    server_address = ('', PORT)
    httpd = ThreadedHTTPServer(server_address, RequestHandler)
    httpd.serve_forever()
</code>
<|/ a tags=python,python-3.x |>
<| a tags=python,python-3.x |>
<code>
import http.server
import socketserver

PORT = 80

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(self.server.url_root)

class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    allow_reuse_address = True

class ThreadedHTTPRequestServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    allow_reuse_address = True

if __name__ == '__main__':
    server_address = ('', PORT)
    httpd = ThreadedHTTPServer(server_address, RequestHandler)
    httpd.serve_forever()
</code>
<|/ a dscore=1 |>
<| a |>
<code>
import http.server
import socketserver

PORT = 80

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(self.server.url_root)

class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    allow_reuse_address = True

class ThreadedHTTPRequestServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    allow_reuse_address = True

if __name__ == '__main__':
    server_address = ('', PORT)
    httpd = ThreadedHTTPServer(server_address, RequestHandler)
    httpd.serve_forever()
</code>
<|/ a dscore