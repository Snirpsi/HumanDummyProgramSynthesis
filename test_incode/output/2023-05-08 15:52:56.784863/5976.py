#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that converts a list of numbers.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    import socket
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes(numbers, 'utf-8'))
            else:
                self.send_error(404)
    
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, Handler)
    
    print('Serving on port 8000...')
    httpd.serve_forever()

