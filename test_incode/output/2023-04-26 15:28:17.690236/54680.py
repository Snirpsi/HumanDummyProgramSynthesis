#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits. """    
    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    from urllib.parse import urlparse
    
    HOST = 'localhost'
    PORT = 8080
    
    class FruitHandler(BaseHTTPRequestHandler):
        """ A simple HTTP handler that converts fruits. """
        
        def do_GET(self):
            """ Handles GET requests. """
            
            path = urlparse(self.path).path
            
            if path == '/':
                """ Handles GET requests. """
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<h1>Fruit Converter</h1>')
                self.wfile.write(b'</body></html>')
                
            elif path == '/fruit':
                """ Handles GET requests. """
                
                fruit = self.path.split('/')[1]
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<h1>' + fruit + '</h1>')
                self.wfile.write(b'</body></html>')
                
            else:
                """ Handles GET requests. """
                
                self.send_error(404)
                
    httpd = HTTPServer((HOST, PORT), FruitHandler)
    httpd.serve_forever()
    
