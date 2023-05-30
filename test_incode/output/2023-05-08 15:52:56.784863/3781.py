#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that requests a list of words.
    #The server will respond with an HTML page listing the words in the
    #given order.
    import os
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import socketserver

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(
                '<html><body>'
                '<ol>%s</ol></body></html>' % '\n'.join(words),
                'utf-8'))

    server_address = ('', 8000)
    httpd = HTTPServer(server_address, Handler)
    httpd.serve_forever()

