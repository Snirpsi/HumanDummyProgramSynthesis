#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers. """    
    from http.server import BaseHTTPRequestHandler
    from urllib.parse import parse_qs
    import math
    import random
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ GET request """
            params = parse_qs(self.path)
            
            number = int(params['number'][0])
            
            answer = math.floor(number / 10) * 10 + math.floor(number % 10) * 10
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(str(answer))
    
    server_address = ('', 8080)
    httpd = BaseHTTPRequestHandler.HTTPServer(server_address, RequestHandler)
    httpd.serve_forever()
    
