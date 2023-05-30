#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    from urllib.parse import urlparse, parse_qs
    from socketserver import ThreadingMixIn
    from sys import argv
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()
    
class MyHandler(BaseHTTPRequestHandler):
    """ A simple HTTP server that enumerates all ports. """
    def do_GET(self):
        """ Respond to a GET request by printing all available ports. """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        parsed_url = urlparse(self.path)
        
        ports = []
        
        for port in range(0, 65535):
            ports.append(port)
        
        ports.sort()
        
        for port in ports:
            self.wfile.write(str(port) + '\n')
        
