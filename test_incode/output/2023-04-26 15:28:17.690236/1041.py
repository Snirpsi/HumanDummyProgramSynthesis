#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port. """    
    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body>')
            self.wfile.write(b'<h1>Hello, world!</h1>')
            self.wfile.write(b'</body></html>')
    
    httpd = HTTPServer(("", 80), RequestHandler)
    httpd.serve_forever()
    
