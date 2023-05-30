#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words or multiplyes user input. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes('<html><body>', 'utf-8'))
                self.wfile.write(bytes('<h1>Hello World</h1>', 'utf-8'))
                self.wfile.write(bytes('</body></html>', 'utf-8'))
            else:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes('<html><body>', 'utf-8'))
                self.wfile.write(bytes('<h1>%s</h1>' % sys.argv[self.path.rfind('/')+1:], 'utf-8'))
                self.wfile.write(bytes('</body></html>', 'utf-8'))
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, Handler)
    
    print('Serving at http://%s:%s/' % (server_address[0], server_address[1]))
    httpd.serve_forever()

<|/ file source=github |>