#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <numbers>" % sys.argv[0])
        sys.exit()
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        try:
            number = int(number)
        except ValueError:
            print("Error! %s is not a number" % number)
            sys.exit()
        
        if number < 0:
            print("Error! %s is negative" % number)
            sys.exit()
        
        if number > sys.maxsize:
            print("Error! %s is too large" % number)
            sys.exit()
        
        if number < -sys.maxsize:
            print("Error! %s is too small" % number)
            sys.exit()
    
