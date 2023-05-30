#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that removes a list of words.
    #It will listen on port 8080 and will respond with a list of all words in the list.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from socketserver import ThreadingMixIn
    from urllib.parse import urlparse
    from io import StringIO
    from random import choice
    from time import sleep
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            if parsed_url.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes(choice(words),"utf8"))
            else:
                self.send_error(404)
    
    server_address = ('localhost', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()

