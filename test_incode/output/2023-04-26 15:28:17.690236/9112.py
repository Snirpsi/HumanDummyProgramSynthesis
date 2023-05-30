#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    from urllib.parse import urlparse
    import socket
    
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()
    
class MyHandler(BaseHTTPRequestHandler):
    """ A simple handler to serve a static file """
    def do_GET(self):
        """ Serve the static file """
        parsed_url = urlparse(self.path)
        
        if parsed_url.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self.