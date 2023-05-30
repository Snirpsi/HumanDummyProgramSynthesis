#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports. """    
    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Return a list of all available ports. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            ports = []
            for port in range(1, 65535):
                ports.append(port)
            
            self.wfile.write(bytes(ports, 'utf8'))
    
    httpd = HTTPServer(("", 80), Handler)
    
    print("Serving on port 80")
    httpd.serve_forever()
    
