#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs
    from io import BytesIO

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            q = parse_qs(
                self.rfile.read(int(self.headers['Content-Length']))
            )
            numbers = q['numbers']
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            for number in numbers:
                self.wfile.write(str(number))
            self.wfile.flush()

    httpd = HTTPServer(("", 8080), Handler)
    httpd.serve_forever()
</code>
<|/ a dscore=0 |>
<| c |>
Thanks, this works great! I 