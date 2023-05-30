#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores numbers or removes numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        if number > 0:
            print('Number %d is greater than zero' % number)
        else:
            print('Number %d is less than zero' % number)
    else:
        print('Usage: %s number' % sys.argv[0])
    
