#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class WebServer(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body>')
            self.wfile.write(b'<h1>Hello World</h1>')
            self.wfile.write(b'</body></html>')
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, WebServer)
    httpd.serve_forever()

<|/ file source=github |>