#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    
    class FruitHandler(BaseHTTPRequestHandler):
        """ A handler for fruits. """
        
        def do_GET(self):
            """ Handle GET requests. """
            
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write(b'<h1>Hello World</h1>')
                return
            
            parsed_path = parsed_url.path.split('/')
            
            if parsed_path[0] == 'fruits':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write(b'<h1>Fruits</h1>')
                return
            
            self.send_error(404)
            return
            
    httpd = HTTPServer(('', 8080), FruitHandler)
    
    print('Serving at http://127.0.0.1:8080/')
    httpd.serve_forever()
    
