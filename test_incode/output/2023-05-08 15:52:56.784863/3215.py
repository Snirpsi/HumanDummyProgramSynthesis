#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that requests a list of words.
    #The server will respond with a list of words and a status code.
    #The status code can be 200 or 404.
    #The response is JSON-encoded.
    import sys
    import os
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from json import dumps
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            if parsed_url.path == '/':
                self.send_response(200)
                self.end_headers()
                self.wfile.write(dumps(words))
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(dumps(words))
    
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, Handler)
    httpd.serve_forever()

