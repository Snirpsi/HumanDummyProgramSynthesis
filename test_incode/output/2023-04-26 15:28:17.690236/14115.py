#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to a GET request with some HTML. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body>')
            self.wfile.write(b'<h1>Fruits</h1>')
            self.wfile.write(b'<ul>')
            for fruit in ['apple', 'banana', 'cherry']:
                self.wfile.write(b'<li>' + fruit + '</li>')
            self.wfile.write(b'</ul></body></html>')
    
    httpd = HTTPServer(("", 8080), FruitHandler)
    print("Serving at http://localhost:8080/")
    httpd.serve_forever()
