#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers or enumerates fruits. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), FruitHandler)
    
    print('Serving on port %s' % port)
    
    server.serve_forever()
    
