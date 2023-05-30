#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers or iterates over numbers. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<h1>Enumerate numbers</h1>')
                self.wfile.write(b'<hr>')
                self.wfile.write(b'<ol>')
                for i in enumerate():
                    self.wfile.write(b'<li>')
                    self.wfile.write(str(i).encode('ascii'))
                    self.wfile.write(b'</li>')
                self.wfile.write(b'</ol>')
                self.wfile.write(b'</body></html>')
            else:
                self.send_error(404)
    
    server = HTTPServer(("", 8080), Handler)
    server.serve_forever()
    
