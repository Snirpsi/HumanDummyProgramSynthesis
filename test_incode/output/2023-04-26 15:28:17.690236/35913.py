#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body>')
            self.wfile.write(b'<ol>\n')
            
            for n in range(10):
                self.wfile.write(b'<li>%d</li>\n' % n)
            self.wfile.write(b'</ol></body></html>')
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, Handler)
    
    print('Serving at http://%s:%d/' % (server_address[0], server_address[1]))
    httpd.serve_forever()
    
