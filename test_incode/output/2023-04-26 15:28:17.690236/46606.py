#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports. """    
    from http.server import BaseHTTPRequestHandler
    from socketserver import ThreadingMixIn
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            for port in range(1, 65535):
                self.wfile.write(b'<html><head><title>Port ' + str(port) + '</title></head>')
                self.wfile.write(b'<body><p>Port ' + str(port) + '</p></body></html>')
                
                self.wfile.flush()
                
    httpd = BaseHTTPRequestHandler()
    httpd.