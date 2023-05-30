#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits and enumerates a list of words. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), FruitHandler)
    
    print('Serving on port %d...' % port)
    httpd.serve_forever()
    
