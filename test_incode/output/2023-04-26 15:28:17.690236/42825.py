#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers and converts a list of words. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs, urlparse
    from random import choice
    from time import sleep
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            path = urlparse(self.path).path
            
            if path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write(
                    '<html><head><title>Simple HTTP Server</title></head>'
                    '<body><p>Hello World!</p></body></html>'
                )
            else:
                
                querystring = parse_qs(urlparse(self.path).query)
                
                number = choice(range(1, 10))
                
                words = [
                    choice(['cat', 'dog', 'mouse', 'horse', 'sheep']),
                    choice(['cat', 'dog', 'mouse', 'horse', 'sheep']),
                    choice(['cat', 'dog', 'mouse', 'horse', 'sheep']),
                    choice(['cat', 'dog', 'mouse', 'horse', 'sheep']),
                    choice(['cat', 'dog', 'mouse', 'horse', 'sheep']),
                    choice(['cat', 'dog', 'mouse', 'horse', 'sheep']),
                    choice(['cat', 'dog', 'mouse', 'horse', 'sheep']),
                    choice(['cat', 'dog', 'mouse', 'horse', 'sheep']),
                    choice(['cat', 'dog', 'mouse', 'horse', 'sheep']),
                    choice(['cat', 'dog', 'mouse', 'horse', 'sheep']),
                    choice(['cat', 'dog', 'mouse', 'horse', 'sheep']),
                    choice(['cat', 'dog', 'mouse', 'horse', 'sheep']),
                    choice(['cat', 'dog', 'mouse', 'horse', 'sheep']),
                    choice(['cat', 'dog', 'mouse', 'horse', 'sheep']),
                    choice(['cat', 'dog', 'mouse', 'horse', 'sheep']),
                    choice(['cat', 'dog', 'mouse', 'horse', 'sheep']),
                    choice(['cat', 'dog', 'mouse', 'horse', 'sheep']),
                    choice(['cat', 'dog', 'mouse', 'horse', 'sheep']),
                    choice(['cat', 'dog', 'mouse', 'horse', 'sheep']),
                    choice(['cat', 'dog', 'mouse', 'horse', 'sheep']),
                    choice(['cat', 'dog', 'mouse', 'horse', 'sheep']),
                    choice(['cat', 'dog', 'mouse', 'horse', 'sheep']),
                    choice(['cat', 'dog', 'mouse', 'horse', 'sheep']),
