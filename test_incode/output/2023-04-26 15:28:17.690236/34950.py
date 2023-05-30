#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from io import BytesIO
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            path = urlparse(self.path).path
            
            if path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write(b'<html><body><h1>Hello World!</h1></body></html>')
                return
            
            if path == '/convert':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                number = self.path.split('/')[1]
                
                number = int(number)
                
                output = BytesIO()
                
                output.write(b'<html><body><h1>Hello World!</h1></body></html>')
                
                output.write(b'<html><body><h1>Hello World!</h1></body></html>')
                
                output.write(b'<html><body><h1>Hello World!</h1></body></html>')
                
                output.write(b'<html><body><h1>Hello World!</h1></body></html>')
                
                output.write(b'<html><body><h1>Hello World!</h1></body></html>')
                
                output.write(b'<html><body><h1>Hello World!</h1></body></html>')
                
                output.write(b'<html><body><h1>Hello World!</h1></body></html>')
                
                output.write(b'<html><body><h1>Hello World!</h1></body></html>')
                
                output.write(b'<html><body><h1>Hello World!</h1></body></html>')
                
                output.write(b'<html><body><h1>Hello World!</h1></body></html>')
                
                output.write(b'<html><body><h1>Hello World!</h1></body></html>')
                
                output.write(b'<html><body><h1>Hello World!</h1></body></html>')
                
                output.write(b'<html><body><h1>Hello World!</h1></body></html>')
                
                output.write(b'<html><body><h1>Hello World!</h1></body></html>')
                
                output.write(b'<html><body><h1>Hello World!</h1></body></html>')
                
                output.write(b'<html><body><h1>Hello World!</h1></body></html>')
                
                output.write(b'<html><body><h1>Hello World!</h1></body></html>')
                
                output.write(b'<html><body><h1>Hello World!</h1></body></html>')
                
