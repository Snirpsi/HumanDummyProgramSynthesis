#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that requests user input.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from socketserver import ThreadingMixIn

    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            query = parsed_url.query
            path = parsed_url.path
            
            if path == '/':
                path = '/index.html'
            
            if path == '/index.html':
                content = open(query, 'rb').read()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(content)
            else:
                self.send_error(404)
    
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    httpd.serve_forever()

