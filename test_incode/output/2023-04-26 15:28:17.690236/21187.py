#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port or removes fruits. """    
    
    port = int(sys.argv[1])
    
    if port > 0:
        
        fruits = ['apple', 'banana', 'cherry']
        
        for fruit in fruits:
            
            print('serving fruit %s' % fruit)
            
            server = HTTPServer(("", port), FruitHandler)
            
            server.serve_forever()
            
    else:
        
        print('serving fruits')
        
        server = HTTPServer(("", 80), FruitHandler)
        
        server.serve_forever()
        
