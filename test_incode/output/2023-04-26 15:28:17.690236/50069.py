#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            port = int(self.path.split(':')[1])
            print('Serving on port ' + str(port))
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write