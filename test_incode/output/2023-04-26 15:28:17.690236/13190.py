#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse, parse_qs
    from io import BytesIO
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            query = parse_qs(parsed_url.query)
            
            number = query['number'][0]
            
            content = BytesIO()
            content.write(number.encode('utf-8'))
            content.seek(0)
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(content.getvalue())
            
    httpd = HTTPServer(('', 8080), MyHandler)
    httpd.serve_forever()
