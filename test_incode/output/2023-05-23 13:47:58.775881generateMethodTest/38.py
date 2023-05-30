#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A minimal webserver that opens ports.
    httpd = HTTPServer(('', 0), MyHandler)
    httpd.serve_forever()
</code>
<|/ a tags=python,sockets,webserver,http,http |>
<| c |>
Thanks for your answer, but this doesn't really answer my question. My question was more about how to implement a webserver that can serve multiple ports.
<|/ c |>
<| c |>
I edited my answer to include a minimal webserver that opens multiple ports.
<|/ c |>
<| c |>
Thanks for your answer, but this doesn't really answer my question. My question was more about how to implement a webserver that can serve multiple ports.
<|/ c |>
<| c |>
I edited my answer to include a minimal webserver that opens multiple ports.
<|/ c |>
<| a |>
I wrote a small python script to serve multiple ports. You can find it here
<code>
#!/usr/bin/python
import socket
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8080
HOST = 'localhost'

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes('<html><head><title>Server Page</title></head>'
                                '<body><p>Hello World</p></body></html>', 'UTF-8'))

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(length)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes('<html><head><title>Server Page</title></head>'
                                '<body><p>Hello World</p></body></html>', 'UTF-8'))

    def log_message(self, format, *args):
        return

if __name__ == '__main__':
    try:
        server = HTTPServer((HOST, PORT), MyHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        sys.exit(0)
</code>
<|/ a tags=python,sockets,webserver,http,http dscore=2 |>
<| c |>
Thanks for your answer, but this doesn't really answer my question. My question was more about how to implement a webserver that can serve multiple ports.
<|/ c |>
<| a tags=python,sockets,webserver,http,http |>
I wrote a small python script to serve multiple ports. You can find it here
<code>
#!/usr/bin/python
import socket
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8080
HOST = 'localhost'

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes('<html><head><title>Server Page</title></head>'
                                '<body><p>Hello World</p></body></html>', 'UTF-8'))

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(length)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes('<html><head><title>Server Page</title></head>'
                                '<body><p>Hello World</p></body></html>', 'UTF-8'))

    def log_message(self, format, *args):
        return

if __name__ == '__main__':
    try:
        server = HTTPServer((HOST, PORT), MyHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        sys.exit(0)
</code>
<|/ a dscore=2 |>
<| a dscore=2 |>
I wrote a small python script to serve multiple ports. You can find it here
<code>
#!/usr/bin/python
import socket
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8080
HOST = 'localhost'

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes('<html><head><title>Server Page</title></head>'
                                '<body><p>Hello World</p></body></html>', 'UTF-8'))

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(length)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes('<html><head><title>Server Page</title></head>'
                                '<body><p>Hello World</p></body></html>', 'UTF-8'))

    def log_message(self, format, *args):
        return

if __name__ == '__main__':
    try:
        server = HTTPServer((HOST, PORT), MyHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        sys.exit(0)
</code>
<|/ a tags=python,sockets,webserver,http,http |>
<| a dscore=1 |>
I wrote a small python script to serve multiple ports. You can find it here
<code>
#!/usr/bin/python
import socket
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8080
HOST = 'localhost'

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes('<html><head><title>Server Page</title></head>'
                                '<body><p>Hello World</p></body></html>', 'UTF-8'))

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(length)
        self.send_response(