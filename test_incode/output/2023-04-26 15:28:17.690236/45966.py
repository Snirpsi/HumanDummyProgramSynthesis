#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    import math

    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            parsed_url = urlparse(self.path)
            query = parsed_url.query
            
            numbers = query.split(',')
            
            numbers = list(map(int, numbers))
            
            product = numbers[0]
            for number in numbers[1:]:
                product *= number
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(str(product))
            
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    
    print('Serving on port 8080...')
    httpd.serve_forever()
