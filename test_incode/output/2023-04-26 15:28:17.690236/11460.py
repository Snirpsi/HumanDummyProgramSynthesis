#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of numbers. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    import random
    
    server_address = ('localhost', 8080)
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                numbers = [random.randint(1, 10) for _ in range(10)]
                
                self.wfile.write(bytes(
                    '<html><body><h1>Random numbers</h1>'
                    '<ul>'
                    '<li>{}</li>'
                    '</ul></body></html>'.format(numbers),
                    'utf-8'
                ))
            else:
                self.send_error(404)
    
    httpd = HTTPServer(server_address, Handler)
    
    print('Starting webserver on port 8080')
    httpd.serve_forever()
    
