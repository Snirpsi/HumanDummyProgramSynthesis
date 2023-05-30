#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers. """    
    
    from http.server import BaseHTTPRequestHandler
    from urllib.parse import parse_qs
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            query = parse_qs(urlparse(self.path).query)
            
            if query['number']:
                number = ''.join(query['number'])
                
                number = ''.join([c for c in number if c.isdigit()])
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write(number.upper())
                
            else:
                self.send_response(400)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write('Invalid query')
                
    httpd = BaseHTTPRequestHandler()
    httpd.