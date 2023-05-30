#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    class Handler(BaseHTTPRequestHandler):
        """ A simple handler for user input. """
        
        def do_GET(self):
            """ Handle GET requests. """
            
            request = self.request
            
            if request.path.startswith('/'):
                path = '/' + request.path[1:]
            else:
                path = '/' + request.path
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(bytes(request.get