#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that enumerates user input.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            q = parse_qs(
                self.headers['QUERY_STRING'].split('?')[1])
            for k, v in q.items():
                print('%s: %s' % (k, v))

    httpd = HTTPServer(('localhost', 8080), Handler)
    httpd.serve_forever()

