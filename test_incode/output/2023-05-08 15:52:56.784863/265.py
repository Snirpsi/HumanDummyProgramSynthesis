#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that returns user input.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from socketserver import ThreadingMixIn

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            query = parsed_url.query
            query = query.split('&')
            query = dict(query)
            query = query.items()
            query = list(query)
            query = sorted(query, key=lambda x: x[0])
            query = query[::-1]
            query = query[:10]
            query = ' '.join(query)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(query)

    server_address = ('', 8080)
    httpd = HTTPServer(server_address, Handler)
    ThreadingMixIn.instance().start()
    httpd.serve_forever()

