#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    
    class Handler(BaseHTTPRequestHandler):
        """ A simple http server that opens numbers. """
        
        def do_GET(self):
            """ Respond to GET requests. """
            
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(self.