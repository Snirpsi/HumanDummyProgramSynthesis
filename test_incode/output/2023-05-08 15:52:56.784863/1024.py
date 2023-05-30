#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that converts numbers.txt into html and displays it
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from io import BytesIO
    import os
    import sys
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html = ''
            
            for number in numbers:
                html += '<p>%s</p>' % number
            
            self.wfile.write(bytes(html, 'utf8'))
    
    httpd = HTTPServer(('', 8000), Handler)
    httpd.serve_forever()

