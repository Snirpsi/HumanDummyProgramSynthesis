#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            numbers = []
            
            numbers.append(int(self.path[1:]))
            
            numbers = numbers * 2
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            self.wfile.write(str(numbers))
            
    httpd = HTTPServer(("", 80), Handler)
    httpd.serve_forever()
    
