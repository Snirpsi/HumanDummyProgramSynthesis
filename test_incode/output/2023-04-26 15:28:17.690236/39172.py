#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from io import BytesIO

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlparse(self.path).path
            if path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<table>')
                self.wfile.write(b'<tr><th>Number</th><th>Result</th></tr>')
                for number in numbers:
                    self.wfile.write(b'<tr><td>%s</td><td>%s</td></tr>' % (number, number))
                self.wfile.write(b'</table></body></html>')
            else:
                self.send_error(404, path)

    server = HTTPServer(('', 8080), Handler)
    server.serve_forever()

<|/ file source=github |>