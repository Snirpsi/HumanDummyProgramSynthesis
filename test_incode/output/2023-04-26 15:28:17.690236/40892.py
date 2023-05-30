#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class RequestHandler(BaseHTTPRequestHandler):
        """ A simple request handler that multiplies all ports. """
        
        def do_GET(self):
            """ Handle a GET request """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write('<html><head><title>Hello World</title></head>')
            self.wfile.write('<body><p>Hello World</p></body></html>')
    
    httpd = HTTPServer(("", 8080), RequestHandler)
    httpd.serve_forever()
