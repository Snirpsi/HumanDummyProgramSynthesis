#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            port = self.server.server_port
            print('http://127.0.0.1:%s' % port)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
    
    httpd = HTTPServer(("", 80), Handler)
    httpd.serve_forever()
