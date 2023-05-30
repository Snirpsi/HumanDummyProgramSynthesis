#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: %s <number1>' % sys.argv[0])
        sys.exit(1)
    
    number1 = int(sys.argv[1])
    
    print('The result is', number1 * number1)
    
