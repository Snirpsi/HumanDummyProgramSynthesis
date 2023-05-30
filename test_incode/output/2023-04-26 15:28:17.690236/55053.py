#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports or stores fruits. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = 8000
    
    httpd = HTTPServer(('', port), FruitHandler)
    
    print('Serving on port %s' % port)
    httpd.serve_forever()
    
