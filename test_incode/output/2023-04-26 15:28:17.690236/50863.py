#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <numbers>" % sys.argv[0])
        sys.exit()
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        number = int(number)
        
        if number < 0:
            print("Error: Negative numbers are not allowed")
            sys.exit()
        
        if number == 0:
            print("Error: Zero is not allowed")
            sys.exit()
        
        if number > sys.maxsize:
            print("Error: Number too big")
            sys.exit()
        
        if number < -sys.maxsize:
            print("Error: Number too small")
            sys.exit()
        
        print(number)
        
