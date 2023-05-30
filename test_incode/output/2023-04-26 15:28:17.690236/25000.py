#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input. """    
    from http.server import BaseHTTPRequestHandler
    from urllib.parse import urlparse
    from io import BytesIO
    import json
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write(b'<html><body>')
                
                while True:
                    data = self.rfile.read(1024)
                    if not data:
                        break
                    self.wfile.write(data)
                
                self.wfile.write(b'</body></html>')
                
                self.wfile.close()
            else:
                self.send_error(404)
    
    httpd = BaseHTTPServer.HTTPServer(('localhost', 8080), Handler)
    httpd.serve_forever()

<|/ file ext=.py |>