#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that converts words.txt into HTML
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import os
    import sys
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = os.path.join(self.path, self.path.lstrip('/'))
            if os.path.isdir(path):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                for filename in os.listdir(path):
                    path = os.path.join(path, filename)
                    if os.path.isfile(path):
                        with open(path) as file:
                            self.wfile.write(file.read())
            else:
                self.send_response(404)
                self.end_headers()
    
    httpd = HTTPServer(('', 8000), Handler)
    httpd.serve_forever()

