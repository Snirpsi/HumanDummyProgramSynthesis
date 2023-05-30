#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that adds user input.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from socketserver import ThreadingMixIn
    from base64 import b64encode
    from base64 import b64decode
    from json import dumps
    from json import loads
    from sys import argv
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/':
                response = 'Hello World!'
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(response.encode())
            else:
                response = 'Invalid path: %s' % parsed_url.path
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(response.encode())
    
    server_address = ('localhost', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    
    print('Serving at http://%s:%s/' % (server_address[0], server_address[1]))
    
    httpd.serve_forever()

