#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            query = parse_qs(urlparse(self.path).query)
            
            numbers = [int(i) for i in query.get('numbers', [])]
            
            numbers_str = ''
            for i in numbers:
                numbers_str += str(i)
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(numbers_str)
    
    httpd = HTTPServer(('', 8080), MyHandler)
    httpd.serve_forever()
