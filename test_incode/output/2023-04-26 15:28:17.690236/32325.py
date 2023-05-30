#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        multiplier = int(sys.argv[1])
        
        print('The product of %d and %d is %d.' % (multiplier, multiplier, multiplier * multiplier))
        
    else:
        print('Usage: %s <multiplier>' % sys.argv[0])
        
