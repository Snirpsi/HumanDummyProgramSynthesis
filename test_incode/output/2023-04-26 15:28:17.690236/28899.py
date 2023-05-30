#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python -m webserver')
        sys.exit(1)
    
    port = sys.argv[1]
    
    print('Serving on port %s' % port)
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to a GET request. """
            
            number = self.path.split('/')[-1]
            
            if number == '':
                print('Error: no number given')
                return
            
            number = int(number)
            
            if number < 0 or number > 1000:
                print('Error: number out of range')
                return
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            self.wfile.write(str(number))
            
    httpd = HTTPServer(('', port), Handler)
    
    print('Serving on port %s' % port)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nExiting...')
        httpd.server_close()
    
