#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port or iterates over fruits. """    
    
    port = int(sys.argv[1])
    
    if port == 0: 
        port = 1
    
    fruits = ['apple', 'banana', 'cherry']
    
    for fruit in fruits:
        print('Serving on port %s' % port)
        
        server = HTTPServer(("", port), FruitHandler)
        server.serve_forever()
        
