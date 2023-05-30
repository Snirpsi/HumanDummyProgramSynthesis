#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that removes a list of numbers.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from socketserver import ThreadingMixIn
    from urllib.parse import urlparse
    from io import StringIO

    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            path = parsed_url.path
            if path == '/':
                numbers = numbers[:]
            elif path == '/remove':
                numbers = numbers[:] #remove all numbers
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes(str(numbers), 'utf-8'))
            else:
                self.send_error(404)
                self.end_headers()

    server_address = ('localhost', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()

