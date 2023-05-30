#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A minimal webserver that removes a http request.
    server = HTTPServer(('', 80), RequestHandler)
    server.serve_forever()

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(self.request.get_data())

def start_server():
    server = HTTPServer(('', 80), RequestHandler)
    server.serve_forever()

if __name__ == '__main__':
    start_server()
</code>
<|/ a dscore=2 |>
<| c |>
Thanks for your answer. Unfortunately, this does not work for me. I am running this on Ubuntu 14.04.
<|/ c |>
<| c |>
I added a working example to my answer.
<|/ c |>
<| c |>
Thanks for your answer. Unfortunately, this does not work for me. I am running this on Ubuntu 14.04.
<|/ c |>
<| c |>
I added a working example to my answer. Try it out and let me know if it works for you.
<|/ c |>
<| c |>
Thanks for your answer. Unfortunately, this does not work for me. I am running this on Ubuntu 14.04.
<|/ c |>
<| a dscore=1 |>
I used this solution to solve my problem:
<code>
#!/usr/bin/python

import BaseHTTPServer
import SocketServer
import urlparse
import os

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse.urlparse(self.path)
        parsed_path = parsed_url.path
        parsed_query = parsed_url.query
        parsed_query_dict = urlparse.parse_qs(parsed_query)
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_dict = parsed_query_dict[0]
        parsed_query_