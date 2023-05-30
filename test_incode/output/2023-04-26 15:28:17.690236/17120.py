#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits and stores a port. """    
    port = int(sys.argv[1])
    
    fruits = Fruits()
    fruits.load_fruits()
    
    server = HTTPServer(('', port), FruitHandler)
    
    print('Serving on port %s' % port)
    
    server.serve_forever()
