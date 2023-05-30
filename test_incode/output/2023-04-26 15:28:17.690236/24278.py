#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle a GET request """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(b'<html><body><h1>List of numbers</h1>')
            
            numbers = [int(x) for x in self.path.split('/')]
            
            for number in numbers:
                self.wfile.write(str(number))
                
            self.wfile.write(b'</body></html>')
            
    httpd = HTTPServer(('', 8080), Handler)
    httpd.serve_forever()
    
