#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <port>' % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    
    class NumbersHandler(SimpleHTTPRequestHandler):
        """ A simple handler for numbers. """
        
        def do_GET(self):
            """ Handle a GET request. """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write('<html><body>')
            self.wfile.write('<table>')
            
            numbers = [int(n) for n in self.path.split('/')]
            
            for n in numbers:
                self.wfile.write('<tr><td>%d</td><td>%d</td></tr>' % (n, n+1))
            
            self.wfile.write('</table></body></html>')
            
    httpd = HTTPServer(('', port), NumbersHandler)
    
    print('Serving on port %s...' % port)
    
    httpd.serve_forever()

<|/ file ext=.py filename=