#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    server_class = HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(b'<html><head><title>Enumerate input</title></head>')
            self.wfile.write(b'<body>')
            
            for line in self.rfile.readlines():
                self.wfile.write(b'<p>' + line + '</p>')
            
            self.wfile.write(b'</body></html>')
            
    server_address = ('', 8080)
    httpd = server_class(server_address, Handler)
    httpd.serve_forever()
