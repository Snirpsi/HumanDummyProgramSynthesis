#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports and returns all ports. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            ports = []
            
            for port in range(0, 65535):
                ports.append(port)
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            self.wfile.write(ports)
            
    server = HTTPServer(("", 0), Handler)
    
    server.serve_forever()
    
