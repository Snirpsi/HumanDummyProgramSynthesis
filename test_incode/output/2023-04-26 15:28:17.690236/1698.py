#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers and returns a port. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body>')
            self.wfile.write(b'<center><h1>Hello World!</h1></center>')
            self.wfile.write(b'</body></html>')
    
    server = HTTPServer(('', 8080), MyHandler)
    server.serve_forever()
