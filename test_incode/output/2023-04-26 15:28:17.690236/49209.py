#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit(1)
    
    port = int(sys.argv[1])
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to GET requests. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(self.