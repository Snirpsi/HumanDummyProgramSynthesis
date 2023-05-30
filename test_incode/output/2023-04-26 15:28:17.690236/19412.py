#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to GET requests. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body>')
            self.wfile.write(b'<center><h1>Numbers</h1></center>')
            self.wfile.write(b'</body></html>')
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, Handler)
    
    print('Serving at http://127.0.0.1:8080')
    httpd.serve_forever()
    
