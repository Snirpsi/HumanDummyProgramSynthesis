#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A minimal webserver that opens all ports.
    httpd = HTTPServer(('',0), Handler)
    httpd.serve_forever()
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for your answer. Unfortunately this doesn't work for me. I'm running this on a raspberry pi 3 with python 3.7.
<|/ c |>
<| c |>
I edited my answer to include a minimal webserver that opens all ports.
<|/ c |>
<| c |>
Thanks for your answer. Unfortunately this doesn't work for me. I'm running this on a raspberry pi 3 with python 3.7.
<|/ c |>
<| c |>
I edited my answer to include a minimal webserver that opens all ports.
<|/ c |>
<| c |>
Thanks for your answer. Unfortunately this doesn't work for me. I'm running this on a raspberry pi 3 with python 3.7.
<|/ c |>
<| a dscore=0 |>
I used this script to run a python script on port 80 on my raspberry pi 3. It works.
<code>
#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import threading
import ssl
from sys import argv

PORT = 80

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        context.load_cert_chain("cert.pem", "key.pem")
        httpd = HTTPServer(('',PORT), Handler)
        httpd.serve_forever()

if __name__ == '__main__':
    ThreadingMixIn.instance().run()
</code>
<|/ a tags=python,raspberry-pi3,https |>
<| c |>
Thanks for your answer. Unfortunately this doesn't work for me. I'm running this on a raspberry pi 3 with python 3.7.
<|/ c |>
<| c |>
I edited my answer to include a minimal webserver that opens all ports.
<|/ c |>
<| a dscore=0 |>
I used this script to run a python script on port 80 on my raspberry pi 3. It works.
<code>
#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import threading
import ssl
from sys import argv

PORT = 80

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        context.load_cert_chain("cert.pem", "key.pem")
        httpd = HTTPServer(('',PORT), Handler)
        httpd.serve_forever()

if __name__ == '__main__':
    ThreadingMixIn.instance().run()
</code>
<|/ a tags=python,raspberry-pi3,https |>
<| a dscore=0 |>
I used this script to run a python script on port 80 on my raspberry pi 3. It works.
<code>
#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import threading
import ssl
from sys import argv

PORT = 80

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        context.load_cert_chain("cert.pem", "key.pem")
        httpd = HTTPServer(('',PORT), Handler)
        httpd.serve_forever()

if __name__ == '__main__':
    ThreadingMixIn.instance().run()
</code>
<|/ a tags=python,raspberry-pi3,https |>
<| a |>
I used this script to run a python script on port 80 on my raspberry pi 3. It works.
<code>
#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import threading
import ssl
from sys import argv

PORT = 80

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        context.load_cert_chain("cert.pem", "key.pem")
        httpd = HTTPServer(('',PORT), Handler)
        httpd.serve_forever()

if __name__ == '__main__':
    ThreadingMixIn.instance().run()
</code>
<|/ a tags=python,raspberry-pi3,https dscore=0 |>
<| a dscore=0 |>
I used this script to run a python script on port 80 on my raspberry pi 3. It works.
<code>
#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import threading
import ssl
from sys import argv

PORT = 80

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        context.load_cert_chain("cert.pem", "key.pem")
        httpd = HTTPServer(('',PORT), Handler)
        httpd.serve