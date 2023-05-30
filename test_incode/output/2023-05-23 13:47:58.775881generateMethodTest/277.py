#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A minimal webserver that returns a http request.
    server = HTTPServer(('localhost', 8080), RequestHandler)
    server.serve_forever()

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(self.server.url)

if __name__ == '__main__':
    #A minimal webserver that returns a http request.
    server = HTTPServer(('localhost', 8080), RequestHandler)
    server.serve_forever()
</code>
<|/ a tags=python,python-3.x,webserver |>
<| c |>
Thank you so much for your help! I really appreciate it!
<|/ c |>
<| c |>
No problem. Glad I could help.
<|/ c |>
<| a dscore=0 |>
I wrote a small program to test the code you posted. It works fine for me. 
<code>
#!/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(self.server.url)

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8080), RequestHandler)
    server.serve_forever()
</code>
<|/ a tags=python,python-3.x,webserver |>
<| c |>
Thank you so much for your help! I really appreciate it!
<|/ c |>
<| a dscore=0 |>
<code>
#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(self.server.url)

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8080), RequestHandler)
    server.serve_forever()
</code>
<|/ a tags=python,python-3.x,webserver |>
<| c |>
Thank you so much for your help! I really appreciate it!
<|/ c |>
<| a tags=python,python-3.x,webserver |>
<code>
#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(self.server.url)

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8080), RequestHandler)
    server.serve_forever()
</code>
<|/ a dscore=0 |>
<| a dscore=0 |>
<code>
#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(self.server.url)

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8080), RequestHandler)
    server.serve_forever()
</code>
<|/ a tags=python,python-3.x,webserver |>
<| a dscore=0 |>
<code>
#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(self.server.url)

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8080), RequestHandler)
    server.serve_forever()
</code>
<|/ a tags=python,python-3.x,webserver |>
<| a tags=python,python-3.x,webserver |>
<code>
#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(self.server.url)

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8080), RequestHandler)
    server.serve_forever()
</code>
<|/ a dscore=0 |>
<| a dscore=0 |>
<code>
#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(self.server.url)

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8080), RequestHandler)
    server.serve_forever()
</code>
<|/ a tags=python,python-3.x,webserver |>
<| a dscore=0 |>
<code>
#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(self.server.url)

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8080), RequestHandler)
    server.serve_forever()
</code>
<|/ a tags=python,python-3.x,webserver |>
<| a dscore=0 |>
<code>
#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class 