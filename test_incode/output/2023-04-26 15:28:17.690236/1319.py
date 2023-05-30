#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers. """    
    port = 8080
    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    class MyHandler(BaseHTTPRequestHandler):
        """ A simple HTTP server. """
        
        def do_GET(self):
            """ Handle a GET request. """
            
            number = self.path.split('/')[-1]
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(str(int(number)))
            
    httpd = HTTPServer(("", port), MyHandler)
    
    print("Serving at port {}".format(port))
    httpd.serve_forever()
    
