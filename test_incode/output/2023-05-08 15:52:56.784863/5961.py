#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that converts a list of numbers.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from socketserver import ThreadingMixIn
    from urllib.parse import urlparse
    from io import BytesIO
    import cgi
    import json
    
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/':
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD':'GET'})
                
                numbers = form.getlist('numbers')
                
                numbers_str = ''
                for number in numbers:
                    numbers_str += str(number) + ','
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str[:-1]
                
                numbers_str = numbers_str

