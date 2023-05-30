#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse, parse_qs

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlparse(self.path).path
            query = parse_qs(urlparse(self.path).query)
            
            if path == '/':
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<ol>')
                for i in query:
                    self.wfile.write(b'<li>{}</li>'.format(i))
                self.wfile.write(b'</ol></body></html>')
            elif path == '/numbers':
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<ol>')
                for i in query:
                    self.wfile.write(b'<li>{}</li>'.format(i))
                self.wfile.write(b'</ol></body></html>')
            else:
                self.send_error(404)
                self.end_headers()

    server_class = HTTPServer
    httpd = server_class(("", 80), Handler)
    httpd.serve_forever()
