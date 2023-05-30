#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Print all available ports. """
            ports = [str(port) for port in range(1, 65535)]
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(ports)
    
    httpd = HTTPServer(("", 0), Handler)
    httpd.serve_forever()
