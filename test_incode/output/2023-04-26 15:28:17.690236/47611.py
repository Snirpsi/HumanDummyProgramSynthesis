#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body>')
            self.wfile.write(b'<h1>Hello world!</h1>')
            self.wfile.write(b'</body></html>')
    
    server = HTTPServer(('localhost', 8080), MyHandler)
    server.serve_forever()
