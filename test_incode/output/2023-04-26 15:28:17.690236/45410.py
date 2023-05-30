#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports and enumerates fruits. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self.server.server_address[1])
    
    httpd = HTTPServer(("", 8000), Handler)
    httpd.serve_forever()
    
