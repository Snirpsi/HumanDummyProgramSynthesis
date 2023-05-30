#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from socketserver import ThreadingMixIn
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body><h1>List of words</h1>')
            
            for word in words:
                self.wfile.write(b'<p>' + word + b'</p>')
            
            self.wfile.write(b'</body></html>')
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, Handler)
    ThreadingMixIn.instance