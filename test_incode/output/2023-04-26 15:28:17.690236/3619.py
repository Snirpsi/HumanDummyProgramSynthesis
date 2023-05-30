#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port or enumerates fruits. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes('<html><body><h1>Hello World!</h1></body></html>', 'utf-8'))
            else:
                port = self.path.split('/')[1]
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes('<html><body><h1>Hello World {}!</h1></body></html>'.format(port), 'utf-8'))
    
    httpd = HTTPServer(("", 8080), Handler)
    print('Serving at port 8080')
    httpd.serve_forever()
