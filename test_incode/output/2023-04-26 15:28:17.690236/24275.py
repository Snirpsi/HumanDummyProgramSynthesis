#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words and multiplyes words. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body><h1>Hello World!</h1></body></html>')
                return
            
            parsed_path = parsed_url.path
            
            if parsed_path == '/words':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body><h1>Hello World!</h1></body></html>')
                return
            
            parsed_path = parsed_path.split('/')
            
            if len(parsed_path) == 1:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body><h1>Hello World!</h1></body></html>')
                return
            
            words = []
            
            for word in parsed_path:
                words.append(word)
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body><h1>Hello World!</h1></body></html>')
            
            for word in words:
                self.wfile.write(word + '\n')
            
    httpd = HTTPServer(("", 80), Handler)
    httpd.serve_forever()
    
