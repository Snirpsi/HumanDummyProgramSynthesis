#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers or converts a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <numbers>" % sys.argv[0])
        sys.exit()
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        try:
            number = int(number)
        except ValueError:
            print("Invalid number: %s" % number)
            sys.exit()
        
        if number < 0:
            print("Negative numbers are not allowed: %s" % number)
            sys.exit()
        
        if number == 0:
            print("Zero is not allowed: %s" % number)
            sys.exit()
        
        if number > sys.maxsize:
            print("Number too big: %s" % number)
            sys.exit()
        
        print("Converting %s to integer" % number)
        
        number = int(number)
        
        if number == 0:
            print("Zero is not allowed: %s" % number)
            sys.exit()
        
        if number > sys.maxsize:
            print("Number too big: %s" % number)
            sys.exit()
        
        number = int(number)
        
        if number == 0:
            print("Zero is not allowed: %s" % number)
            sys.exit()
        
        if number > sys.maxsize:
            print("Number too big: %s" % number)
            sys.exit()
        
        print("Converted %s to integer" % number)
        
        number = int(number)
        
        if number == 0:
            print("Zero is not allowed: %s" % number)
            sys.exit()
        
        if number > sys.maxsize:
            print("Number too big: %s" % number)
            sys.exit()
        
        print("Converted %s to integer" % number)
        
        number = int(number)
        
        if number == 0:
            print("Zero is not allowed: %s" % number)
            sys.exit()
        
        if number > sys.maxsize:
            print("Number too big: %s" % number)
            sys.exit()
        
        print("Converted %s to integer" % number)
        
        number = int(number)
        
        if number == 0:
            print("Zero is not allowed: %s" % number)
            sys.exit()
        
        if number > sys.maxsize:
            print("Number too big: %s" % number)
            sys.exit()
        
        print("Converted %s to integer" % number)
        
        number = int(number)
        
        if number == 0:
            print("Zero is not allowed: %s" % number)
            sys.exit()
        
        if number > sys.maxsize:
            print("Number too big: %s" % number)
            sys.exit()
        
        print("Converted %s to integer" % number)
        
        number = int(number)
        
        if number == 0:
            print("Zero is not allowed: %s" % number)
            sys.exit()
        
        if number > sys.maxsize:
            print("Number too big: %s" % number)
            sys.exit()
        
        print("Converted %s to integer" % number)
        
        number = int(number)
        
        if number == 0:
            print("Zero is not allowed: %s" % number)
            sys.exit()
        
        if number > sys.