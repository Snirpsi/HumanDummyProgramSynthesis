#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports or enumerates numbers. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to GET requests. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body>')
            
            for port in range(1, 65535):
                self.wfile.write(b'<p>Port {}</p>'.format(port))
            
            self.wfile.write(b'</body></html>')
            
    httpd = HTTPServer(('localhost', 0), Handler)
    httpd.serve_forever()
    
