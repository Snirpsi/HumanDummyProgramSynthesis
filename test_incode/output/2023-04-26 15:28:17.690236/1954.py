#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs, urlparse
    import cgi

    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            q = urlparse(self.path)
            if q.path == '/':
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={
                        'REQUEST_METHOD': 'GET',
                        'QUERY_STRING': q.query,
                    })
                numbers = [int(n) for n in form.getvalue().split(',')]
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(str(numbers))
            else:
                self.send_error(404)

    server = HTTPServer(('', 8080), MyHandler)
    server.serve_forever()
</code>
<|/ a dscore=0 tags=python,webserver,python-3.x |>
<| c |>
Thanks for the answer. I'm still a beginner in python so I still have some questions. What is `cgi.FieldStorage`? And how do I get the numbers from the form and store them in a list?
<|/ c |>
<| c |>
`cgi.FieldStorage` parses the request body and stores the values into the `FieldStorage` object. `FieldStorage` objects have a `get` method that returns a `list` of strings. `cgi.FieldStorage` also has a `getlist` method that returns a `list` of strings. `cgi.FieldStorage` also has a `getvalue` method that returns a string. `cgi.FieldStorage` also has a `getall` method that returns a `dict` of strings to strings.
<|/ c |>
<| c |>
I edited my answer to include a complete example. Hope it helps.
<|/ c |>
<| c |>
Thanks again. I'm still getting an error when trying to run the code though. `Traceback (most recent call last):
  File "/home/pi/Desktop/testserver.py", line 9, in <module>
    form = cgi.FieldStorage(
AttributeError: 'module' object has no attribute 'FieldStorage'`
<|/ c |>
<| c |>
I edited my answer to include a complete example. Hope it helps.
<|/ c |>
<| a tags=python,webserver,python-3.x |>
I used this code to solve my problem:
<code>
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
import cgi

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        q = urlparse(self.path)
        if q.