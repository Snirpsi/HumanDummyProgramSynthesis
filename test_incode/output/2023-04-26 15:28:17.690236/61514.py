#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port or calculates a list of numbers. """    
    
    port = int(sys.argv[1])
    
    if port < 1:
        port = 80
    
    numbers = range(port)
    
    numbers_str = ','.join(map(str, numbers))
    
    print('Serving on port %s' % port)
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    httpd.serve_forever()
    
