#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words. """    
    import sys
    port = sys.argv[1]
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            words = []
            
            words.append('Hello World!')
            words.append('Goodbye World!')
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            self.wfile.write(bytes(