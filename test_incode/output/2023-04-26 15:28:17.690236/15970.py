#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers or iterates over a port. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    from socketserver import ThreadingMixIn
    from urllib.parse import urlparse
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            if parsed_url.path == '/':
                path = '/index.html'
            elif parsed_url.path == '/index.html':
                path = '/index.html'
            else:
                path = self.path
            
            if parsed_url.query:
                path += '?' + parsed_url.query
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(open(path).read())
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    
    ThreadingMixIn.