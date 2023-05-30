#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A minimal webserver that adds a port.
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    print("Serving at port", port)
    httpd.serve_forever()
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for your answer. I'm new to python and I didn't know that you could use port 8080 like that. I'll try it out and see how it goes.
<|/ c |>
<| c |>
I added the port 8080 line to the code you gave me. Now when I try to run it I get this error: `File "server.py", line 4, in <module>
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
  File "/usr/lib/python3.4/http/server.py", line 72, in __init__
    BaseHTTPServer.__init__(self,server_address, RequestHandlerClass)
  File "/usr/lib/python3.4/socketserver.py", line 598, in __init__
    self.server_bind()
  File "/usr/lib/python3.4/socketserver.py", line 324, in server_bind
    self.socket.bind(self.server_address)
  File "/usr/lib/python3.4/socket.py", line 224, in meth
    return getattr(self._sock,name)(*args)
socket.error: [Errno 98] Address already in use`
<|/ c |>
<| c |>
I added the port 8080 line to the code you gave me. Now when I try to run it I get this error: `File "server.py", line 4, in <module>
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
  File "/usr/lib/python3.4/http/server.py", line 72, in __init__
    BaseHTTPServer.__init__(self,server_address, RequestHandlerClass)
  File "/usr/lib/python3.4/socketserver.py", line 598, in __init__
    self.server_bind()
  File "/usr/lib/python3.4/socketserver.py", line 324, in server_bind
    self.socket.bind(self.server_address)
  File "/usr/lib/python3.4/socket.py", line 224, in meth
    return getattr(self._sock,name)(*args)
socket.error: [Errno 98] Address already in use`
<|/ c |>
<| c |>
I added the port 8080 line to the code you gave me. Now when I try to run it I get this error: `File "server.py", line 4, in <module>
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
  File "/usr/lib/python3.4/http/server.py", line 72, in __init__
    BaseHTTPServer.__init__(self,server_address, RequestHandlerClass)
  File "/usr/lib/python3.4/socketserver.py", line 598, in __init__
    self.server_bind()
  File "/usr/lib/python3.4/socketserver.py", line 324, in server_bind
    self.socket.bind(self.server_address)
  File "/usr/lib/python3.4/socket.py", line 224, in meth
    return getattr(self._sock,name)(*args)
socket.error: [Errno 98] Address already in use`
<|/ c |>
<| c |>
I added the port 8080 line to the code you gave me. Now when I try to run it I get this error: `File "server.py", line 4, in <module>
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
  File "/usr/lib/python3.4/http/server.py", line 72, in __init__
    BaseHTTPServer.__init__(self,server_address, RequestHandlerClass)
  File "/usr/lib/python3.4/socketserver.py", line 598, in __init__
    self.server_bind()
  File "/usr/lib/python3.4/socketserver.py", line 324, in server_bind
    self.socket.bind(self.server_address)
  File "/usr/lib/python3.4/socket.py", line 224, in meth
    return getattr(self._sock,name)(*args)
socket.error: [Errno 98] Address already in use`
<|/ c |>
<| a |>
I fixed the problem by changing my code to the following:
<code>
#!/usr/bin/python
import http.server
import socketserver
port = 8080
class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Hello World</title></head><body>Hello World</body></html>", "utf-8"))

if __name__ == '__main__':
    httpd = socketserver.TCPServer(("", port), SimpleHTTPRequestHandler)
    print("Serving at port", port)
    httpd.serve_forever()
</code>
<|/ a dscore=0 tags=python,python-3.x,socketserver |>
<| c |>
This doesn't work for me. I'm getting `File "server.py", line 4, in <module>
    httpd = socketserver.TCPServer(("", port), SimpleHTTPRequestHandler)
  File "/usr/lib/python3.4/socketserver.py", line 72, in __init__
    BaseHTTPServer.__init__(self,server_address, RequestHandlerClass)
  File "/usr/lib/python3.4/http/server.py", line 72, in __init__
    BaseHTTPServer.__init__(self,server_address, RequestHandlerClass)
  File "/usr/lib/python3.4/socketserver.py", line 598, in __init__
    self.server_bind()
  File "/usr/lib/python3.4/socketserver.py", line 324, in server_bind
    self.socket.bind(self.server_address)
  File "/usr/lib/python3.4/socket.py", line 224, in meth
    return getattr(self._sock,name)(*args)
socket.error: [Errno 98] Address already in use`
<|/ c |>
<| c |>
I fixed the problem by changing my code to the following:
<|/ c |>
<| c |>
I fixed the 