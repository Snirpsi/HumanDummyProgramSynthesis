#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            number = self.path.split('/')[-1]
            
            if number == '':
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write('No number given.')
                return
            
            number = int(number)
            
            if number < 0 or number > 10:
                self.send_response(400)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write('Invalid number.')
                return
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write('The number is: %s' % number)
            
    httpd = HTTPServer(("", 8080), RequestHandler)
    
    print("Serving at http://localhost:8080/numbers/")
    httpd.serve_forever()
    
