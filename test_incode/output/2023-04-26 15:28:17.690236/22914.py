#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port %s' % port)
    httpd.serve_forever()
    
