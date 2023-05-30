#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port. """    
    from http.server import BaseHTTPRequestHandler
    from socketserver import ThreadingMixIn
    
    class RequestHandler(BaseHTTPRequestHandler):
        """ A simple request handler that enumerates ports. """
        def do_GET(self):
            """ Enumerates ports. """
            ports = []
            for port in range(0, 65535):
                ports.append(port)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(ports, 'utf8'))
    
    server_address = ('', 8080)
    httpd = ThreadingMixIn(Server