#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input. """    
    
    from http.server import BaseHTTPRequestHandler
    from socketserver import ThreadingMixIn
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body>')
            self.wfile.write(b'<form action="/" method="post">')
            self.wfile.write(b'<input type="text" name="user">')
            self.wfile.write(b'<input type="submit">')
            self.wfile.write(b'</form>')
            self.wfile.write(b'</body></html>')
    
    server = ThreadingMixIn(BaseHTTPRequestHandler, Handler)
    
    server_address = ('', 8080)
    
    httpd = 