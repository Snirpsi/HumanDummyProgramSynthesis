#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: python %s <port>' % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            path = urllib.parse.unquote(self.path)
            
            if path == '/':
                path = '/index.html'
                
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(bytes(open(path, 'rb').read(), 'utf-8'))
    
    server = HTTPServer(('', port), Handler)
    
    print('Serving on port %s' % port)
    
    server.serve_forever()
    
