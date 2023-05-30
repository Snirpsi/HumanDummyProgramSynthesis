#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that requests user input.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from socketserver import ThreadingMixIn

    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            query = parsed_url.query
            path = parsed_url.path
            query = query.split('&')
            for item in query:
                key, value = item.split('=')
                query[key] = value.strip()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(query, 'utf8'))

    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    ThreadingMixIn.instance().start()
    httpd.serve_forever()

