#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        """ A simple handler that opens numbers. """
        def do_GET(self):
            """ Open a web page that opens numbers. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            numbers = [int(x) for x in self.path.split('/') if x]
            
            for number in numbers:
                self.wfile.write(str(number))
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, Handler)
    
    httpd.serve_forever()

<|/ file ext=.py |>