#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <number1>' % sys.argv[0])
        exit(1)
    
    number1 = sys.argv[1]
    
    number2 = number1 * number1
    
    print('The product of %s and %s is %s' % (number1, number2, number1 * number1))
    
