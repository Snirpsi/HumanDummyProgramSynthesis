#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <num1> <num2>' % sys.argv[0])
        sys.exit()
    
    num1 = sys.argv[1]
    num2 = sys.argv[2]
    
    print('The product of %d and %d is %d.' % (num1, num2, num1 * num2))
    
