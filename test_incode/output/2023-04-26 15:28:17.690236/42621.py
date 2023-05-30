#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            words = self.path.split('/')
            
            if len(words) == 2:
                word = words[1]
                
                if word in words:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/plain')
                    self.end_headers()
                    self.wfile.write(words[word])
                else:
                    self.send_response(404)
                    self.end_headers()
            else:
                self.send_response(404)
                self.end_headers()
        
    httpd = HTTPServer(('localhost', 8000), Handler)
    