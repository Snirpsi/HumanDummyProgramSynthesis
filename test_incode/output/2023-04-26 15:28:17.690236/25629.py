#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers. """    
    
    port = 8080
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            numbers = range(10)
            
            for number in numbers:
                self.wfile.write(str(number))
            
    httpd = HTTPServer(("", port), RequestHandler)
    
    print("Serving at port", port)
    
    httpd.serve_forever()
    
