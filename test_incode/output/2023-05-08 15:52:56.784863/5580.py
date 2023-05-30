#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that opens user input.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlparse(self.path).path
            if path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(self.server.server_version + '\n')
                self.wfile.write(self.server.server_name + '\n')
                self.wfile.write(self.server.server_url + '\n')
                self.wfile.write(self.server.server_url + '/\n')
                self.wfile.write(self.server.server_url + '/index.html\n')
            else:
                self.send_error(404)
    
    httpd = HTTPServer(('', 8080), Handler)
    httpd.serve_forever()

