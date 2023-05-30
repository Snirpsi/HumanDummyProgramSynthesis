#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports or opens user input. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path.endswith('/'):
                port = self.path.split('/')[1]
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes(f'<html><head><title>{port}</title></head><body>'))
                self.wfile.write(bytes(f'<p>Open a browser to see your port</p>'))
                self.wfile.write(bytes(f'<p><a href="http://localhost:{port}/">http://localhost:{port}/</a></p>'))
                self.wfile.write(bytes(f'<p><a href="http://localhost:{port}/open">http://localhost:{port}/open</a></p>'))
                self.wfile.write(bytes(f'</body></html>'))
            else:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes(f'<html><head><title>Open a browser to see your port</title></head><body>'))
                self.wfile.write(bytes(f'<p>Open a browser to see your port</p>'))
                self.wfile.write(bytes(f'<p><a href="http://localhost:{port}/">http://localhost:{port}/</a></p>'))
                self.wfile.write(bytes(f'<p><a href="http://localhost:{port}/open">http://localhost:{port}/open</a></p>'))
                self.wfile.write(bytes(f'</body></html>'))
    
    httpd = HTTPServer(("", 8080), Handler)
    httpd.serve_forever()
    
