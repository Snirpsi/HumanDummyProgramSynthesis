#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    from urllib.parse import urlparse
    from socketserver import ThreadingMixIn
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<h1>Hello World!</h1>')
            else:
                self.send_error(404)
                self.end_headers()
    
    server_address = ('localhost', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    
    ThreadingMixIn.