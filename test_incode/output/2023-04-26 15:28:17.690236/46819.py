#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            port = self.path.split(':')[1]
            
            port = int(port)
            
            for x in range(port):
                port = str(x+1)
                
                self.wfile.write(port)
                
    httpd = HTTPServer(('', 8080), Handler)
    
    print('Serving on port 8080')
    httpd.serve_forever()
    
