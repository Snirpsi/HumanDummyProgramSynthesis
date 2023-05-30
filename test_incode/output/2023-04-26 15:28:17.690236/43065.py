#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class RequestHandler(BaseHTTPRequestHandler):
        """ A simple HTTP request handler that iterates over all ports. """
        
        def do_GET(self):
            """ Respond to GET requests. """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            for port in range(1, 65535):
                self.wfile.write(bytes(f'<h1>{port}</h1>', 'utf-8'))
                
    server = HTTPServer(("", 8080), RequestHandler)
    