#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that calculates user input.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from socketserver import ThreadingMixIn
    from time import sleep

    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            path = parsed_url.path
            query = parsed_url.query
            
            if path == '/':
                response = 'Hello, world!'
            elif path == '/hello':
                response = 'Hello, %s!' % query
            elif path == '/sleep':
                sleep(float(query))
            else:
                response = 'Invalid path: %s' % path
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(response.encode('utf-8'))

    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    ThreadingMixIn.instance().start()
    httpd.serve_forever()

