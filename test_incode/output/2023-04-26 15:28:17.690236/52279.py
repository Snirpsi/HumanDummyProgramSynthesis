#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body>')
            for line in self.rfile.readlines():
                self.wfile.write(line)
            self.wfile.write(b'</body></html>')
    
    httpd = HTTPServer(("", 80), Handler)
    httpd.serve_forever()
