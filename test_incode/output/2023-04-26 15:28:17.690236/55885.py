#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qsl, urlparse
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            query_string = parse_qsl(parsed_url.query)
            
            numbers = query_string.get('numbers', None)
            
            if numbers is None:
                self.send_response(400)
                self.end_headers()
                return
            
            numbers = [int(x) for x in numbers.split(',')]
            
            numbers_sum = 0
            for number in numbers:
                numbers_sum += number
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(str(numbers_sum))
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    
    print('Starting httpserver on port 8080...')
    httpd.serve_forever()
