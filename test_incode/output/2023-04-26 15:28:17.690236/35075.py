#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port or converts fruits. """    
    
    import sys
    
    ports = [int(p) for p in sys.argv[1:]]
    
    for port in ports:
        print('Port %d' % port)
        
        if port > 65535:
            print('Port %d is too large.' % port)
            sys.exit(1)
    
    fruits = ['apple', 'banana', 'cherry']
    
    for fruit in fruits:
        print('Fruit %s' % fruit)
        
        if fruit not in fruits:
            print('Fruit %s is not in the fruits list.' % fruit)
            sys.exit(1)
    
    print('Done.')
    
