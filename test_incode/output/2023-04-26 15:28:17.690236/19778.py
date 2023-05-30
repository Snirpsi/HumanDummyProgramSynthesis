#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs
    import socket
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to GET requests. """
            query = parse_qs(self.path)
            
            words = query['words']
            
            words = words.split(',')
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            for word in words:
                self.wfile.write(word + '\n')
            
            self.wfile.flush()
            
    httpd = HTTPServer(("", 80), Handler)
    
    print("Serving on port 80")
    httpd.serve_forever()
    
