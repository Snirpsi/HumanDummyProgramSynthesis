#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports. """    
    
    from http.server import BaseHTTPRequestHandler
    from socketserver import ThreadingMixIn
    from urllib.parse import urlparse
    
    class RequestHandler(BaseHTTPRequestHandler):
        """ A simple request handler that iterates over all ports. """
        
        def do_GET(self):
            """ Handle a GET request. """
            
            parsed_url = urlparse(self.path)
            
            if parsed_url.port == 80:
                port = 80
            elif parsed_url.port == 443:
                port = 443
            else:
                port = parsed_url.port
                
            for port in range(port, 65535):
                self.send_response(port)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write(self.