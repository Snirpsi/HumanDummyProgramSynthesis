#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports and enumerates all ports. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            parsed_url = urlparse(self.path)
            
            if parsed_url.port == 80:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<p>This port is open.</p>')
                self.wfile.write(b'</body></html>')
            elif parsed_url.port == 443:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<p>This port is open.</p>')
                self.wfile.write(b'</body></html>')
            else:
                self.send_error(404)
                self.end_headers()
                
    httpd = HTTPServer(("", 80), MyHandler)
    httpd.serve_forever()
    
