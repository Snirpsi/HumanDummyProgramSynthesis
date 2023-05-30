#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(b'<html><body>')
            self.wfile.write(b'<h1>Enumerate all ports</h1>')
            self.wfile.write(b'</body></html>')
    
    httpd = HTTPServer(('', 0), Handler)
    
    print('Serving at http://127.0.0.1:8000/')
    httpd.serve_forever()
    
