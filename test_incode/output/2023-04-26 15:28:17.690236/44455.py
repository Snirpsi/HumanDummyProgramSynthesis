#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to a GET request. """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            self.wfile.write(b'Hello, World!\n')
    
    httpd = HTTPServer(("", 8000), RequestHandler)
    
    print("Serving at port 8000...")
    httpd.serve_forever()
    
