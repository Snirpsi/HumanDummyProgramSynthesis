#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input or adds a port. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from socketserver import ThreadingMixIn
    from urllib.parse import urlparse
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/':
                """ Root page. """
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write(self.server.root_html)
                
            elif parsed_url.path == '/add':
                """ Add new user. """
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write(self.server.root_html)
                
            elif parsed_url.path == '/port':
                """ Add new user. """
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write(self.server.root_html)
                
            else:
                """ Unknown request. """
                
                self.send_response(404)
                self.end_headers()
                
                self.wfile.write(self.server.root_html)
                
    class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
        """ A threaded HTTP server. """
        
        def __init__(self, server_address, RequestHandlerClass):
            """ Initialize server. """
            
            HTTPServer.__init__(self, server_address, RequestHandlerClass)
            
            self.