#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body>')
            self.wfile.write(b'<ol>')
            
            numbers = []
            for i in range(10):
                numbers.append(i)
            
            self.wfile.write(b'<li>')
            for number in numbers:
                self.wfile.write(b'%s</li>' % number)
            
            self.wfile.write(b'</ol>')
            self.wfile.write(b'</body></html>')
    
    httpd = HTTPServer(("", 80), Handler)
    
    print("Serving at port 80...")
    httpd.serve_forever()
    
