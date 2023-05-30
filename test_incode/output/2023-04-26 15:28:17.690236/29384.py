#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers and iterates over all ports. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Prints numbers and iterates over all ports. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            numbers = range(1,100)
            for port in numbers:
                self.wfile.write(str(port) + '\n')
            self.wfile.close()
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, Handler)
    
    print('Serving on port 8080')
    httpd.serve_forever()
