#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body>')
            self.wfile.write(b'<ol>')
            for word in self.words:
                self.wfile.write(b'<li>%s</li>' % word)
            self.wfile.write(b'</ol></body></html>')
    
    server = HTTPServer(('', 8000), Handler)
    server.serve_forever()
