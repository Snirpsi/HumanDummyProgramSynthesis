#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Returns all ports. """
            ports = []
            
            for port in range(1, 65535):
                ports.append(port)
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(ports)
            
    httpd = HTTPServer(("", 0), RequestHandler)
    httpd.serve_forever()
