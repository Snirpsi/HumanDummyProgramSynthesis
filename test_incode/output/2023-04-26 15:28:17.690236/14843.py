#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes numbers and prints fruits. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), FruitHandler)
    print('Serving on port %s' % port)
    httpd.serve_forever()
    
