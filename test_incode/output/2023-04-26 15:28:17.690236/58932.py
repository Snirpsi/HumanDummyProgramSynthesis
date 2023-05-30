#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            number = self.path.split('/')[-1]
            
            if number == '':
                number = '1'
            
            number = int(number)
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(str(number))
            
    httpd = HTTPServer(("", 8000), Handler)
    
    httpd.serve_forever()
    
