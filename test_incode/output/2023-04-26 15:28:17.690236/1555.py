#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port. """    
    import sys
    port = int(sys.argv[1])
    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Prints a port """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(str(port))
    
    httpd = HTTPServer(('', port), Handler)
    httpd.serve_forever()
