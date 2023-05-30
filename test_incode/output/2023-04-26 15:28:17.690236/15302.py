#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle a GET request """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes('<html><head><title>Enumerate Port</title></head><body>Enumerate Port</body></html>', 'utf-8'))
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, Handler)
    
    print('Starting webserver on port 8000...')
    httpd.serve_forever()
    
