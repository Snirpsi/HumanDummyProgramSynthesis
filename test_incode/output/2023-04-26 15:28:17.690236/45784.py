#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to GET requests. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body>')
            self.wfile.write(b'<h1>Hello world!</h1>')
            self.wfile.write(b'</body></html>')
    
    httpd = HTTPServer(("", 8080), Handler)
    httpd.serve_forever()
    
