#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port or prints numbers. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from socketserver import ThreadingMixIn
    from socket import AF_INET, SOCK_STREAM

    server_address = ('localhost', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()

class MyHandler(BaseHTTPRequestHandler):
    """ A simple HTTP server that prints numbers. """
    def do_GET(self):
        """ Handle GET requests. """
        parsed_url = urlparse(self.path)
        port = parsed_url.port
        if port is not None:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(str(port))
        else:
            self.send_error(404)
            self.end_headers()

if __name__ == '__main__':
    