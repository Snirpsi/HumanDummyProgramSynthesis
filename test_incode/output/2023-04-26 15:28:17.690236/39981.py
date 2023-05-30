#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            number = self.path[1:]
            
            if number:
                numbers = list(range(int(number)))
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                for number in numbers:
                    self.wfile.write(str(number))
            else:
                self.send_error(404)
    
    server = HTTPServer(("", 80), Handler)
    
    print("Serving on port 80")
    server.serve_forever()
    
