#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class RequestHandler(BaseHTTPRequestHandler):
        """ A simple request handler that multiplies all ports. """
        
        def do_GET(self):
            """ A GET request that multiplies all ports. """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(self.server.port*2)
            
    httpd = HTTPServer(("", 8080), RequestHandler)
    httpd.serve_forever()
    
