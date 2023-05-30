#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers or stores a port. """    
    
    port = int(sys.argv[1])
    
    if port > 65535:
        print('Port must be less than 65535')
        sys.exit()
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    print('Serving on port %s' % port)
    httpd.serve_forever()
    
