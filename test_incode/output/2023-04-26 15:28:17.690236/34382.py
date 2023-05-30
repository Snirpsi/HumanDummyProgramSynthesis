#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port. """    
    port = 8080
    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(f'<h1>{port}</h1>', 'utf-8'))
    
    httpd = HTTPServer(("", port), Handler)
    
    httpd.serve_forever()
    
