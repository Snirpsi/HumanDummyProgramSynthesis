#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A minimal webserver that removes ports.
    httpd = HTTPServer(("", 0), Handler)
    httpd.serve_forever()
</code>
<|/ a dscore=1 |>
<| c |>
This doesn't work for me. I'm getting `AttributeError: 'HTTPServer' object has no attribute 'server'`
<|/ c |>
<| c |>
I edited my answer to include a minimal webserver that removes ports.
<|/ c |>
<| c |>
This doesn't work for me. I'm getting `AttributeError: 'HTTPServer' object has no attribute 'server'`
<|/ c |>
<| c |>
I edited my answer to include a minimal webserver that removes ports.
<|/ c |>
<| c |>
This doesn't work for me. I'm getting `AttributeError: 'HTTPServer' object has no attribute 'server'`
<|/ c |>
<| a dscore=0 |>
I used this code to remove ports from my server:
<code>
import http.server
import socketserver
import ssl

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        ports = [666,8080,80,443,22,3]
        httpd = socketserver.TCPServer(("", ports.pop()), Handler)
        httpd.serve_forever()

if __name__ == "__main__":
    httpd = socketserver.TCPServer(("", 443), Handler)
    httpd.serve_forever()
</code>
<|/ a tags=python,python-3.x,httpserver |>
<| c |>
This doesn't work for me. I'm getting `AttributeError: 'HTTPServer' object has no attribute 'server'`
<|/ c |>
<| c |>
I edited my answer to include a minimal webserver that removes ports.
<|/ c |>
<| a dscore=0 |>
I used this code to remove ports from my server:
<code>
import http.server
import socketserver
import ssl

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        ports = [666,8080,80,443,22,3]
        httpd = socketserver.TCPServer(("", ports.pop()), Handler)
        httpd.serve_forever()

if __name__ == "__main__":
    httpd = socketserver.TCPServer(("", 443), Handler)
    httpd.serve_forever()
</code>
<|/ a tags=python,python-3.x,httpserver |>
<| a tags=python,python-3.x,httpserver |>
I used this code to remove ports from my server:
<code>
import http.server
import socketserver
import ssl

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        ports = [666,8080,80,443,22,3]
        httpd = socketserver.TCPServer(("", ports.pop()), Handler)
        httpd.serve_forever()

if __name__ == "__main__":
    httpd = socketserver.TCPServer(("", 443), Handler)
    httpd.serve_forever()
</code>
<|/ a dscore=0 |>
<| a dscore=0 |>
I used this code to remove ports from my server:
<code>
import http.server
import socketserver
import ssl

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        ports = [666,8080,80,443,22,3]
        httpd = socketserver.TCPServer(("", ports.pop()), Handler)
        httpd.serve_forever()

if __name__ == "__main__":
    httpd = socketserver.TCPServer(("", 443), Handler)
    httpd.serve_forever()
</code>
<|/ a tags=python,python-3.x,httpserver |>
<| a |>
I used this code to remove ports from my server:
<code>
import http.server
import socketserver
import ssl

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        ports = [666,8080,80,443,22,3]
        httpd = socketserver.TCPServer(("", ports.pop()), Handler)
        httpd.serve_forever()

if __name__ == "__main__":
    httpd = socketserver.TCPServer(("", 443), Handler)
    httpd.serve_forever()
</code>
<|/ a tags=python,python-3.x,httpserver dscore=0 |>
<| a tags=python,python-3.x,httpserver |>
<code>
import http.server
import socketserver
import ssl

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        ports = [666,8080,80,443,22,3]
        httpd = socketserver.TCPServer(("", ports.pop()), Handler)
        httpd.serve_forever()

if __name__ == "__main__":
    httpd = socketserver.TCPServer(("", 443), Handler)
    httpd.serve_forever()
</code>
<|/ a dscore=0 |>
<| a tags=python,python-3.x,httpserver |>
<code>
import http.server
import socketserver
import ssl

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        ports = [666,8080,80,443,22,3]
        httpd = socketserver.TCPServer(("", ports.pop()), Handler)
        httpd.serve_forever()

if __name__ == "__main__":
    httpd = socketserver.TCP