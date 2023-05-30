#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            numbers = range(10)
            
            for number in numbers:
                self.wfile.write(str(number))
            
    httpd = HTTPServer(('', 8080), Handler)
    
    print('Serving on port 8080...')
    httpd.serve_forever()
    
