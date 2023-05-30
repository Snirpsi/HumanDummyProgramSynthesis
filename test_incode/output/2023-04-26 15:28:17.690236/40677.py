#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(b'<html><body><h1>Fruits</h1>')
            
            fruits = ['apple', 'banana', 'cherry']
            for fruit in fruits:
                self.wfile.write(b'<div>' + fruit + b'</div>')
            
            self.wfile.write(b'</body></html>')
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, FruitHandler)
    
    print('Starting webserver on port 8080')
    httpd.serve_forever()
    
