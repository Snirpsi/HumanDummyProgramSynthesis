#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port or converts all ports. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = '80'
    
    httpd = HTTPServer(('', int(port)), SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port %s ...' % port)
    httpd.serve_forever()
    
