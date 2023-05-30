#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <numbers>" % sys.argv[0])
        sys.exit()
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        number = int(number)
        
        if number < 0:
            print("Error: negative numbers not allowed")
            sys.exit()
        
        if number == 0:
            print("Error: zero numbers allowed")
            sys.exit()
        
        if number > sys.maxsize:
            print("Error: number too large")
            sys.exit()
    
    print("Done")

<|/ file filename=