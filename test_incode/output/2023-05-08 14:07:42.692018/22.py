#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A minimal webserver that requests a port.
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
</code>
<|/ a tags=python,flask,webserver |>
<| c |>
Thanks for your answer. I am not familiar with flask but will try to learn it soon. Do you know if there is a way to run this script without flask?
<|/ c |>
<| c |>
Yes, you can run it without Flask. Just replace `app.run()` with `httpd.serve_forever()`
<|/ c |>
<| c |>
Thanks again. Do you know if there is a way to run this script without flask? I mean without using flask but using only python and sockets.
<|/ c |>
<| c |>
Yes, you can run it without Flask. Just replace `app.run()` with `httpd.serve_forever()`
<|/ c |>
<| c |>
Thanks again. Do you know if there is a way to run this script without flask? I mean without using flask but using only python and sockets.
<|/ c |>
<| a dscore=0 |>
<code>
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<h1>Hello World</h1>')

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
    server.serve_forever()
</code>
<|/ a tags=python,flask,webserver |>
<| c |>
Thanks for your answer. I am not familiar with flask but will try to learn it soon. Do you know if there is a way to run this script without flask?
<|/ c |>
<| c |>
Yes, you can run it without Flask. Just replace `app.run()` with `httpd.serve_forever()`
<|/ c |>
<| c |>
Thanks again. Do you know if there is a way to run this script without flask? I mean without using flask but using only python and sockets.
<|/ c |>
<| c |>
Yes, you can run it without Flask. Just replace `app.run()` with `httpd.serve_forever()`
<|/ c |>
<| c |>
Thanks again. Do you know if there is a way to run this script without flask? I mean without using flask but using only python and sockets.
<|/ c |>
<| a tags=python,flask,webserver |>
<code>
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<h1>Hello World</h1>')

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
    server.serve_forever()
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for your answer. I am not familiar with flask but will try to learn it soon. Do you know if there is a way to run this script without flask?
<|/ c |>
<| c |>
Yes, you can run it without Flask. Just replace `app.run()` with `httpd.serve_forever()`
<|/ c |>
<| c |>
Thanks again. Do you know if there is a way to run this script without flask? I mean without using flask but using only python and sockets.
<|/ c |>
<| c |>
Yes, you can run it without Flask. Just replace `app.run()` with `httpd.serve_forever()`
<|/ c |>
<| c |>
Thanks again. Do you know if there is a way to run this script without flask? I mean without using flask but using only python and sockets.
<|/ c |>
<| a dscore=0 |>
<code>
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<h1>Hello World</h1>')

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
    server.serve_forever()
</code>
<|/ a tags=python,flask,webserver |>
<| c |>
Thanks for your answer. I am not familiar with flask but will try to learn it soon. Do you know if there is a way to run this script without flask?
<|/ c |>
<| c |>
Yes, you can run it without Flask. Just replace `app.run()` with `httpd.serve_forever()`
<|/ c |>
<| c |>
Thanks again. Do you know if there is a way to run this script without flask? I mean without using flask but using only python and sockets.
<|/ c |>
<| c |>