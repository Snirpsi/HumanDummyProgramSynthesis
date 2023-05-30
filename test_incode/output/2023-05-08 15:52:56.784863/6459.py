#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that converts numbers.txt into HTML
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from io import BytesIO
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            file = BytesIO()
            file.write(self.headers['Content-type'])
            file.write(self.headers['Content-Length'])
            file.write(self.rfile.read(int(
                self.headers['Content-Length'])))
            file.seek(0)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            file.write(file.read())
    httpd = HTTPServer(('', 8080), Handler)
    httpd.serve_forever()

