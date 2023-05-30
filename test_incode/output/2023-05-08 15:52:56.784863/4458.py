#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that enumerates user input.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            q = parse_qs(
                self.headers['QUERY_STRING'],
                keep_blank_values=True
            )
            q = q['q']
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(q)

    httpd = HTTPServer(('', 8080), Handler)
    httpd.serve_forever()

