#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports. """    
    
    from http.server import BaseHTTPRequestHandler
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Return all ports. """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            ports = []
            for port in range(0, 65535):
                ports.append(port)
            
            self.wfile.write(bytes(ports, 'utf-8'))
            
    server_address = ('', 8080)
    httpd = BaseHTTPServer.HTTPServer(server_address, Handler)
    httpd.serve_forever()
    
