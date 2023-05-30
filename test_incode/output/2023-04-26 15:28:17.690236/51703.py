#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits. """    
    
    import os
    
    port = int(os.getenv('PORT', 8080))
    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Remove a fruit from the list. """
            
            fruit = self.path.split('/')[-1]
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(
                '<html><head><title>Remove fruit: %s</title></head>'
                '<body><p>The fruit %s has been removed.</p></body></html>'
                % (fruit, fruit)
            )
    
    server = HTTPServer(('', port), RequestHandler)
    
    print('Serving at port %s' % port)
    
    server.serve_forever()
    
