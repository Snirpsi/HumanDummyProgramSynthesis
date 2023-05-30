#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port. """    
    port = 8080
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><head><title>Port</title></head>')
            self.wfile.write(b'<body><p>Port is %d' % port)
            self.wfile.write(b'</body></html>')
    
    httpd = HTTPServer(('', port), Handler)
    httpd.serve_forever()
    
