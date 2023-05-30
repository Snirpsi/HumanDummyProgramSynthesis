#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that opens fruits.html and displays them in fruirs.html
    import os
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    import cgi
    
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlparse(self.path).path
            if path == "/fruits.html":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(fruirs)
            elif path == "/fruirs.html":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(fruirs)
            else:
                self.send_error(404)
                self.end_headers()
    
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, FruitHandler)
    
    httpd.serve_forever()
</code>
<|/ a dscore=1 |>
<| c |>
Thanks for the answer. I'll try it out and let you know how it goes.
<|/ c |>
<| c |>
It works perfectly. Thanks so much!
<|/ c |>
<| c |>
Glad it helped. :)
<|/ c |>
<| a dscore=0 |>
<code>
#!/usr/bin/python3
#A minimal webserver that opens fruits.html and displays them in fruirs.html
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import cgi
    
class FruitHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/fruits.html":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(fruirs)
        elif path == "/fruirs.html":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(fruirs)
        else:
            self.send_error(404)
            self.end_headers()
    
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, FruitHandler)
    
    httpd.serve_forever()
</code>
<|/ a tags=python,html,webserver |>
<| c |>
Please explain your answer.
<|/ c |>
<| c |>
I added the explanation to the answer
<|/ c |>
<| c |>
Thanks for the answer. I'll try it out and let you know how it goes.
<|/ c |>
<| a dscore=0 |>
<code>
#!/usr/bin/python3
#A minimal webserver that opens fruits.html and displays them in fruirs.html
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import cgi
    
class FruitHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/fruits.html":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(fruirs)
        elif path == "/fruirs.html":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(fruirs)
        else:
            self.send_error(404)
            self.end_headers()
    
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, FruitHandler)
    
    httpd.serve_forever()
</code>
<|/ a tags=python,html,webserver |>
<| c |>
Please explain your answer.
<|/ c |>
<| c |>
I added the explanation to the answer
<|/ c |>
<| a |>
<code>
#!/usr/bin/python3
#A minimal webserver that opens fruits.html and displays them in fruirs.html
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import cgi
    
class FruitHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/fruits.html":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(fruirs)
        elif path == "/fruirs.html":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(fruirs)
        else:
            self.send_error(404)
            self.end_headers()
    
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, FruitHandler)
    
    httpd.serve_forever()
</code>
<|/ a dscore=0 tags=python,html,webserver |>
<| c |>
Please explain your answer.
<|/ c |>
<| a dscore=0 |>
<code>
#!/usr/bin/python3
#A minimal webserver that opens fruits.html and displays them in fruirs.html
import os
from 