#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A minimal webserver that iterates over ports.
    server = HTTPServer(("", ports[0]), Handler)
    server.serve_forever()
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for your answer. I am not able to run this on my local machine. I am getting this error: `AttributeError: 'HTTPServer' object has no attribute 'server_name'`
<|/ c |>
<| c |>
I edited my answer to include a minimal webserver that iterates over ports.
<|/ c |>
<| c |>
Thanks for your answer. I am not able to run this on my local machine. I am getting this error: `AttributeError: 'HTTPServer' object has no attribute 'server_name'`
<|/ c |>
<| c |>
I edited my answer to include a minimal webserver that iterates over ports.
<|/ c |>
<| c |>
Thanks for your answer. I am not able to run this on my local machine. I am getting this error: `AttributeError: 'HTTPServer' object has no attribute 'server_name'`
<|/ c |>
<| a dscore=0 |>
I wrote a small python script to test your code. 
<code>
import http.server
import socketserver

PORT = 8080

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes("<html><body>Hello World</body></html>", 'utf-8'))

if __name__ == "__main__":
    server = socketserver.TCPServer(("", PORT), Handler)
    server.serve_forever()
</code>
I ran the script and got the following output:
<code>
$ python3 server.py
Serving HTTP on 0.0.0.0 port 8080
<html><body>Hello World</body></html>
</code>
<|/ a tags=python,python-3.x,sockets |>
<| c |>
Thanks for your answer. I am not able to run this on my local machine. I am getting this error: `AttributeError: 'HTTPServer' object has no attribute 'server_name'`
<|/ c |>
<| c |>
I ran the script and got the following output: `Serving HTTP on 0.0.0.0 port 8080
<html><body>Hello World</body></html>`
<|/ c |>
<| c |>
I ran the script and got the following output: `Serving HTTP on 0.0.0.0 port 8080
<html><body>Hello World</body></html>`
<|/ c |>
<| c |>
I ran the script and got the following output: `Serving HTTP on 0.0.0.0 port 8080
<html><body>Hello World</body></html>`
<|/ c |>
<| c |>
I ran the script and got the following output: `Serving HTTP on 0.0.0.0 port 8080
<html><body>Hello World</body></html>`
<|/ c |>
<| a dscore=0 |>
I wrote a small python script to test your code. 
<code>
import http.server
import socketserver

PORT = 8080

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes("<html><body>Hello World</body></html>", 'utf-8'))

if __name__ == "__main__":
    server = socketserver.TCPServer(("", PORT), Handler)
    server.serve_forever()
</code>
I ran the script and got the following output:
<code>
Serving HTTP on 0.0.0.0 port 8080
<html><body>Hello World</body></html>
</code>
<|/ a tags=python,python-3.x,sockets |>
<| c |>
Thanks for your answer. I am not able to run this on my local machine. I am getting this error: `AttributeError: 'HTTPServer' object has no attribute 'server_name'`
<|/ c |>
<| c |>
I ran the script and got the following output: `Serving HTTP on 0.0.0.0 port 8080
<html><body>Hello World</body></html>`
<|/ c |>
<| c |>
I ran the script and got the following output: `Serving HTTP on 0.0.0.0 port 8080
<html><body>Hello World</body></html>`
<|/ c |>
<| c |>
I ran the script and got the following output: `Serving HTTP on 0.0.0.0 port 8080
<html><body>Hello World</body></html>`
<|/ c |>
<| c |>
I ran the script and got the following output: `Serving HTTP on 0.0.0.0 port 8080
<html><body>Hello World</body></html>`
<|/ c |>
<| a dscore=0 |>
I wrote a small python script to test your code. 
<code>
import http.server
import socketserver

PORT = 8080

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes("<html><body>Hello World</body></html>", 'utf-8'))

if __name__ == "__main__":
    server = socketserver.TCPServer(("", PORT), Handler)
    server.serve_forever()
</code>
I ran the script and got the following output:
<code>
