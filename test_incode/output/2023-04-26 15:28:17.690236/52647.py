#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    from socketserver import ThreadingMixIn
    
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, MultiplyHandler)
    httpd.serve_forever()
    
class MultiplyHandler(BaseHTTPRequestHandler):
    """ A simple handler for multiplying two numbers. """
    def do_GET(self):
        """ Handle GET requests. """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(str(self.