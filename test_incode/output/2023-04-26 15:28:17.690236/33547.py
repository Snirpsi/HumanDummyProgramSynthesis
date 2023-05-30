#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlparse(self.path).path
            if path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<ol>\n')
                self.wfile.write(b'<li>')
                self.wfile.write(b'<a href="/">Home</a>')
                self.wfile.write(b'</li>\n')
                self.wfile.write(b'<li>')
                self.wfile.write(b'<a href="/numbers">Numbers</a>')
                self.wfile.write(b'</li>\n')
                self.wfile.write(b'<li>')
                self.wfile.write(b'<a href="/about">About</a>')
                self.wfile.write(b'</li>\n')
                self.wfile.write(b'</ol>\n')
                self.wfile.write(b'</body></html>')
            else:
                self.send_error(404)
    
    httpd = HTTPServer(("", 80), Handler)
    httpd.serve_forever()
