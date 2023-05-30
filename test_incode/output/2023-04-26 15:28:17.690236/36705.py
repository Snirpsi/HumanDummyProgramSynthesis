#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port or enumerates all ports. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 5000
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port %s' % port)
    httpd.serve_forever()
    
