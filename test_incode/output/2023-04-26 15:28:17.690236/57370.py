#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words or adds words. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse, parse_qs
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<h1>Hello World!</h1>')
            elif parsed_url.path == '/add':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<h1>Hello World!</h1>')
            elif parsed_url.path == '/multiply':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<h1>Hello World!</h1>')
            else:
                self.send_error(404)
                self.end_headers()
        
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Starting httpserver on port 8080')
    httpd.serve_forever()
