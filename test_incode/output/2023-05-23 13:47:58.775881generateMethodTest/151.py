#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that opens fruits.html on port 80
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlparse(self.path).path
            if path == "/":
                path = "/fruits.html"
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(open(fruirs[int(self.path.split("/fruits")[1])], "rb").read())
    server = HTTPServer(('', 80), FruitHandler)
    server.serve_forever()
</code>
<|/ a dscore=1 |>
<| c |>
Thanks for your answer! I didn't know about `cgi.FieldStorage`, but it's really interesting! I'll try it out and see how it goes.
<|/ c |>
<| c |>
It works perfectly! Thanks again!
<|/ c |>
<| a tags=cgi,python |>
I used the code from https://stackoverflow.com/a/1534814/1412994 and it worked for me. 
<code>
#!/usr/bin/env python
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgitb.enable()
import http.server
import os
import sys
import cgi
import cgitb
cgit