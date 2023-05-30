#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that opens words.txt and displays it.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import os
    import sys
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(bytes(open(sys.argv[1],'r').read(),'utf-8'))
    
    httpd = HTTPServer(('localhost', 8000), Handler)
    httpd.serve_forever()

