#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            ports = [p for p in self.server.sockets]
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            for port in ports:
                self.wfile.write(port.getsockname())
                self.wfile.write('\n')
            
            self.wfile.flush()
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    
    httpd.serve_forever()
