#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port. """    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port %s' % port)
    httpd.serve_forever()
