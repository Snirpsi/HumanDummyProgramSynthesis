#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from io import BytesIO
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            path = urlparse(self.path).path
            
            if path == '/':
                """ Return index.html. """
                
                content = BytesIO(
                    bytes('<html><head><title>Multiply</title></head>'
                        '<body><p>Multiply words!</p></body></html>',
                        'utf8'))
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write(content.getvalue())
                
            elif path == '/multiply':
                """ Return multiply.html. """
                
                content = BytesIO(
                    bytes('<html><head><title>Multiply</title></head>'
                        '<body><p>Multiply words!</p></body></html>',
                        'utf8'))
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write(content.getvalue())
                
            else:
                """ Return 404 error. """
                
                self.send_response(404)
                self.end_headers()
                
                self.wfile.write(bytes('404 Not Found', 'utf8'))
                
    httpd = HTTPServer(('', 8080), Handler)
    
    print('Serving on port 8080...')
    httpd.serve_forever()
    
