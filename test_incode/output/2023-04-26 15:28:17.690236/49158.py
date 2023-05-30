#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port. """    
    from http.server import BaseHTTPRequestHandler
    from socketserver import ThreadingMixIn
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle a GET request """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(b'<html><head><title>Hello World!</title></head>')
            self.wfile.write(b'<body><p>Hello World!</p></body></html>')
            
    server_address = ('', 8080)
    httpd = ThreadingMixIn(server_address, MyHandler)
    httpd.serve_forever()
    
