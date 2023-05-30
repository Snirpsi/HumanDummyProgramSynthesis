#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers and calculates fruits. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), FruitCalculator)
    print('Serving on port %s' % port)
    httpd.serve_forever()
    
