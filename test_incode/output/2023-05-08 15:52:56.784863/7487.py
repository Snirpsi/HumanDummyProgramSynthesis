#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that converts a list of numbers.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from io import BytesIO
    import cgi

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            path = parsed_url.path
            if path == '/':
                path = '/index.html'
            
            form = cgi.FieldStorage(fp=self.rfile, headers=self.headers,
                environ={'REQUEST_METHOD':'GET'})
            
            numbers = form.getlist('numbers')
            
            numbers_str = ''
            for number in numbers:
                numbers_str += str(number) + ','
            numbers_str = numbers_str[:-1]
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(numbers_str)
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, Handler)
    httpd.serve_forever()

