#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Convert numbers to strings. """
            
            number = self.path.split('/')[-1]
            
            if number.isdigit():
                number = '%d' % int(number)
                
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(number.encode('utf-8'))
    
    server = HTTPServer(('localhost', 8080), RequestHandler)
    
    server.serve_forever()
