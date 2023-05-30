#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers. """    
    import sys
    from http.server import BaseHTTPRequestHandler
    from urllib.parse import parse_qs, urlparse
    import random
    import math
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle a GET request. """
            
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write(
                    "<html><head><title>Simple Web Server</title></head>"
                    "<body>"
                    "<h1>Simple Web Server</h1>"
                    "<p>This web server converts a list of numbers to an "
                    "HTML page. Try it out by visiting this page: "
                    "<a href=\"http://localhost:8000\">http://localhost:8000</a></p>"
                    "</body></html>"
                    )
            else:
                
                qs = parse_qs(parsed_url.query)
                
                nums = [random.randint(1, 100) for _ in range(len(qs))]
                
                html = ''
                
                for num in nums:
                    html += "<p> %d </p>" % num
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write(html)
                
    httpd = BaseHTTPRequestHandler()
    httpd.