#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes user input or converts words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        if sys.argv[1] == '--help':
            
            print('Usage: %s [--help]' % sys.argv[0])
            
            sys.exit(0)
            
        else:
            
            multiplier = int(sys.argv[1])
            
    else:
        
        multiplier = int(input('Enter a number: '))
        
    print('Multiplication of %d and %d is %d' % (multiplier, multiplier, multiplier * multiplier))
    
