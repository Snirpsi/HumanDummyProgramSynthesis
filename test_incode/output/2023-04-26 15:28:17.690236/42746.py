#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes('<html><head><title>Port 8080</title></head><body><p>Port 8080</p></body></html>', 'UTF-8'))
    
    httpd = HTTPServer(('localhost', 8080), Handler)
    print('Serving at http://localhost:8080')
    httpd.serve_forever()
    
