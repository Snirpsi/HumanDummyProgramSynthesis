#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits and prints numbers. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), FruitHandler)
    
    print('Serving at port %s' % port)
    
    httpd.serve_forever()
    
