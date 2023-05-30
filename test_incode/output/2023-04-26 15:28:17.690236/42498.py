#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers and multiplyes numbers. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs
    import math

    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            query = parse_qs(self.path)
            numbers = query['numbers']
            numbers = [int(x) for x in numbers]
            numbers = [x * y for x, y in zip(numbers, numbers)]
            numbers = [math.floor(x) for x in numbers]
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(
                '<html><head><title>Multiplication Example</title></head>'
                '<body><p>Multiplication Example</p>'
                '<p>Numbers: {}</p>'
                '<p>Result: {}</p>'
                '</body></html>'.format(*numbers))

    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    print('Starting httpd on port 8000...')
    httpd.serve_forever()
