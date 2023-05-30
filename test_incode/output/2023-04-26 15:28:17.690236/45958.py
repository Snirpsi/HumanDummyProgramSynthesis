#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port or converts words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write('<html><body>')
                self.wfile.write('<h1>Hello world</h1>')
                self.wfile.write('</body></html>')
            else:
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(self.path)
    
    httpd = HTTPServer(("", 8080), Handler)
    httpd.serve_forever()

<|/ file filename=server.py ext=.py |>