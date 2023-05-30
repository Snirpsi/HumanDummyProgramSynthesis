#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers. """    
    from http.server import BaseHTTPRequestHandler
    from urllib.parse import parse_qs
    from math import prod
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ GET request. """
            args = parse_qs(self.path)
            
            numbers = args.get('numbers', [])
            
            numbers = [int(x) for x in numbers]
            
            product = prod(numbers)
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(str(product))
            
    httpd = BaseHTTPRequestHandler()
    httpd.