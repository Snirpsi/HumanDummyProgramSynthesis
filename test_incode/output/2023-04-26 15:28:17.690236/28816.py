#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers. """    
    import sys
    from http.server import BaseHTTPRequestHandler
    from urllib.parse import parse_qs, urlparse
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                
                numbers = parse_qs(parsed_url.query)
                
                for number in numbers:
                    self.wfile.write(b'<p>%s</p>' % number)
                
                self.wfile.write(b'</body></html>')
            else:
                self.send_error(404)
    
    httpd = BaseHTTPRequestHandler()
    httpd.