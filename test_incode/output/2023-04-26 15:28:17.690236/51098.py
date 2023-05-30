#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words. """    
    from http.server import BaseHTTPRequestHandler
    from urllib.parse import urlparse
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<h1>Hello World!</h1>')
                self.wfile.write(b'</body></html>')
            else:
                self.send_error(404)
    
    server_address = ('', 8080)
    httpd = BaseHTTPServer.HTTPServer(server_address, Handler)
    