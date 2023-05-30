#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import socketserver
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            words = open('words.txt').read().splitlines()
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            for word in words:
                self.wfile.write(word + '\n')
            
    httpd = HTTPServer(('', 8080), Handler)
    
    print('Serving on port 8080...')
    httpd.serve_forever()
