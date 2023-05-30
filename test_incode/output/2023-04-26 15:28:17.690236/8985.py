#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python %s number" % sys.argv[0])
        sys.exit(0)
    
    number = sys.argv[1]
    
    try:
        number = int(number)
    except ValueError:
        print("Usage: python %s number" % sys.argv[0])
        sys.exit(0)
    
    result = number * number
    
    print("The product of %d and %d is %d." % (number, number, result))
    
