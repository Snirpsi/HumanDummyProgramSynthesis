#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input and prints words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python webserver.py <port>')
        sys.exit()
    
    port = sys.argv[1]
    
    print('Serving on port %s' % port)
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            path = urllib.parse.unquote(self.path)
            
            if path == '/':
                path = '/index.html'
            
            if path == '/index.html':
                content = '<h1>Hello World</h1>'
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write(content)
            else:
                content = '<h1>Not Found</h1>'
                
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write(content)
    
    httpd = HTTPServer(("", port), RequestHandler)
    
    print('Serving on port %s' % port)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nExiting.')
        httpd.server_close()
    
    print('\nStopped.')
    
