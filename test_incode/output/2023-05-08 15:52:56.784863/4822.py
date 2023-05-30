#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that adds user input.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    import cgi
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlparse(self.path).path
            if path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<form action="/add" method="post">')
                self.wfile.write(b'<input type="text" name="name">')
                self.wfile.write(b'<input type="submit" value="Add">')
                self.wfile.write(b'</form>')
                self.wfile.write(b'</body></html>')
            else:
                self.send_error(404)
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    httpd.serve_forever()

