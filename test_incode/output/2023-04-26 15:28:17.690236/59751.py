#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ GET request """
            
            number = self.path.split('/')[1]
            
            if number:
                number = int(number)
                
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                
                self.wfile.write(str(number))
            else:
                self.send_error(400, 'No number given')
    
    server = HTTPServer(('', 8000), RequestHandler)
    server.serve_forever()
    
