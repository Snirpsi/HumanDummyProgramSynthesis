#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class RequestHandler(BaseHTTPRequestHandler):
        """ A simple request handler that converts user input. """
        def do_GET(self):
            """ Handle a GET request. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>Hello, world!</h1>')
    
    httpd = HTTPServer(("", 80), RequestHandler)
    print("Serving on port 80")
    httpd.serve_forever()
    
