#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes user input. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 %s <number1>" % sys.argv[0])
        sys.exit()
    
    number1 = int(sys.argv[1])
    
    print("The product of %d and %d is %d." % (number1, number1, number1 * number1))
    
