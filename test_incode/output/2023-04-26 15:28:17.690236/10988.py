#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits or iterates over words. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle a GET request. """
            
            if self.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<h1>Hello, world!</h1>')
                return
            
            if self.path == '/fruit':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<h1>Fruits:</h1>')
                self.wfile.write(b'<ul>')
                for fruit in ['apple', 'banana', 'cherry']:
                    self.wfile.write(b'<li>%s</li>' % fruit)
                self.wfile.write(b'</ul>')
                return
            
            if self.path == '/word':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<h1>Words:</h1>')
                self.wfile.write(b'<ul>')
                for word in ['apple', 'banana', 'cherry']:
                    self.wfile.write(b'<li>%s</li>' % word)
                self.wfile.write(b'</ul>')
                return
            
            if self.path == '/':
                self.send_error(404)
                return
            
            self.send_error(404)
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    
    print('Starting server...')
    httpd.serve_forever()

<|/ file ext=.py |>