#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port. """    
    import sys
    port = int(sys.argv[1])
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self.