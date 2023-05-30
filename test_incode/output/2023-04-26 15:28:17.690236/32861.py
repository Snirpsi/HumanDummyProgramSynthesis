#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits or iterates over a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8000
    
    httpd = HTTPServer(('', port), FruitHandler)
    
    print('Serving on port %d' % port)
    httpd.serve_forever()
    
