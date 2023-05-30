#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that converts words.txt into HTML
    from http.server import BaseHTTPRequestHandler, HTTPServer
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('words.txt', 'r') as f:
                for word in f.read().split():
                    self.wfile.write(word + '\n')
    httpd = HTTPServer(('', 8080), Handler)
    httpd.serve_forever()

