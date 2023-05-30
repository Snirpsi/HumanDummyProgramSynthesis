#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input. """    
    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    from urllib.parse import parse_qs, urlparse
    import socket
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/':
                response = '<h1>Hello World!</h1>'
                self.send_response(200)
                self.end_headers()
                self.wfile.write(response.encode())
                return
            
            params = parse_qs(parsed_url.query)
            
            if params:
                response = params['q'][0]
            else:
                response = '<h1>No query string given!</h1>'
            
            self.send_response(200)
            self.end_headers()
            self.wfile.write(response.encode())
    
    server_address = ('localhost', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    
    print('Starting web server on port 8080')
    httpd.serve_forever()
