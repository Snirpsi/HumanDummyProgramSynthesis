#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <numbers>" % sys.argv[0])
        sys.exit(0)
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        try:
            number = int(number)
        except ValueError:
            print("Error: %s is not a number" % number)
            sys.exit(1)
        
        if number < 0:
            print("Error: %s is negative" % number)
            sys.exit(1)
        
        number = abs(number)
        
        if number > sys.maxint:
            print("Error: %s is too big" % number)
            sys.exit(1)
        
        if number < -sys.maxint:
            print("Error: %s is too small" % number)
            sys.exit(1)
        
        print(number)
        
