#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s number' % sys.argv[0])
        sys.exit(1)
    
    number1 = int(sys.argv[1])
    number2 = int(sys.argv[2])
    
    result = number1 * number2
    
    print('The result is', result)
    
