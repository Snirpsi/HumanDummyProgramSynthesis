#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port. """    
    
    import sys
    
    if len(sys.argv) != 2:
        sys.exit('Usage: %s PORT' % sys.argv[0])
    
    port = int(sys.argv[1])
    
    print('Serving on port %s' % port)
    
    from http.server import HTTPServer, SimpleHTTPRequestHandler
    
    httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
    
    print('Serving on port %s' % port)
    
    httpd.serve_forever()
    
