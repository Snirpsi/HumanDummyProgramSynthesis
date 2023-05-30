#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of numbers. """    
    port = int(sys.argv[1])
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    server.serve_forever()
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for your answer. I'm new to python and I didn't know that you could do that. I'll try it out and see how it goes.
<|/ c |>
<| c |>
I added the code I used to test it out to my answer. Hope it helps.
<|/ c |>
<| c |>
I added the code I used to test it out to my answer. Hope it helps.
<|/ c |>
<| c |>
Thanks so much! I appreciate your help. I really appreciate it!
<|/ c |>
<| c |>
You're welcome. Glad I could help. If this answer helped you, please consider marking it as accepted (click the check mark next to the answer).
<|/ c |>
<| a tags=python,flask,flask-restful |>
I used the code below to test it out. Hope it helps.
<code>
from flask import Flask, request
from http.server import HTTPServer, BaseHTTPRequestHandler

app = Flask(__name__)
port = int(sys.argv[1])
server = HTTPServer(('', port), BaseHTTPRequestHandler)

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<h1>Hello World</h1>')

if __name__ == '__main__':
    server.serve_forever()
</code>
<|/ a d