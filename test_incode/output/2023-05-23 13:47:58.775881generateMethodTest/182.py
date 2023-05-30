#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A minimal webserver that opens a http request.
    httpd = BaseHTTPServer.HTTPServer(('localhost', 80), RequestHandler)
    httpd.serve_forever()
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for the reply, but this doesn't work. I'm getting a 404 error when I try to access http://snirps.ddns.net/
<|/ c |>
<| c |>
I added a working example to my answer. Try it out and let me know if it works for you.
<|/ c |>
<| c |>
Thanks again, that works perfectly. One more question, how would I go about making the server listen on port 80? I've tried adding `httpd.listen(80)` but that doesn't seem to work.
<|/ c |>
<| c |>
I added a working example to my answer. Try it out and let me know if it works for you.
<|/ c |>
<| c |>
Thanks again, that works perfectly. One more question, how would I go about making the server listen on port 80? I've tried adding `httpd.listen(80)` but that doesn't seem to work.
<|/ c |>
<| a dscore=0 |>
I wrote a small python script to listen on port 80 and then open a browser to that port using subprocess. 
<code>
import subprocess
port = int(input("Enter the port you want to listen on: "))
subprocess.call(["open", "http://127.0.0.1:"+str(port)])
</code>
<|/ a tags=python,webserver,python-3.x |>
<| a dscore=0 |>
<code>
import http.server
import socketserver
import ssl

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        html = "<html><body>"
        html += "<h1>Hello World</h1>"
        html += "</body></html>"
        self.wfile.write(bytes(html, 'utf-8'))

class SSLHandler(socketserver.BaseRequestHandler):
    def do_GET(self):
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        context.load_cert_chain('cert.pem', 'key.pem')
        server = socketserver.TCPServer(("", 443), RequestHandler)
        server.socket = context.wrap_socket(self.request.socket, server_side=True)
        server.serve_forever()

if __name__ == "__main__":
    server = SSLHandler()
    server.serve_forever()
</code>
<|/ a tags=python,webserver,python-3.x |>
<| a dscore=0 |>
I wrote a small python script to listen on port 80 and then open a browser to that port using subprocess. 
<code>
import subprocess
port = int(input("Enter the port you want to listen on: "))
subprocess.call(["open", "http://127.0.0.1:"+str(port)])
</code>
<|/ a tags=python,webserver,python-3.x |>
<| a tags=python,webserver,python-3.x |>
<code>
import http.server
import socketserver
import ssl

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        html = "<html><body>"
        html += "<h1>Hello World</h1>"
        html += "</body></html>"
        self.wfile.write(bytes(html, 'utf-8'))

class SSLHandler(socketserver.BaseRequestHandler):
    def do_GET(self):
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        context.load_cert_chain('cert.pem', 'key.pem')
        server = socketserver.TCPServer(("", 443), RequestHandler)
        server.socket = context.wrap_socket(self.request.socket, server_side=True)
        server.serve_forever()

if __name__ == "__main__":
    server = SSLHandler()
    server.serve_forever()
</code>
<|/ a dscore=0 |>
<| a tags=python,webserver,python-3.x |>
<code>
import http.server
import socketserver
import ssl

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        html = "<html><body>"
        html += "<h1>Hello World</h1>"
        html += "</body></html>"
        self.wfile.write(bytes(html, 'utf-8'))

class SSLHandler(socketserver.BaseRequestHandler):
    def do_GET(self):
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        context.load_cert_chain('cert.pem', 'key.pem')
        server = socketserver.TCPServer(("", 443), RequestHandler)
        server.socket = context.wrap_socket(self.request.socket, server_side=True)
        server.serve_forever()

if __name__ == "__main__":
    server = SSLHandler()
    server.serve_forever()
</code>
<|/ a dscore=0 |>
<| a dscore=0 |>
<code>
import http.server
import socketserver
import ssl

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        html = "<html><body>"
        html += "<h1>Hello World</h1>"
        