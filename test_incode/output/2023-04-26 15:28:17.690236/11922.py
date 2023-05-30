#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 remove-numbers.py <numbers>")
        sys.exit()
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        number = int(number)
        
        if number < 1:
            print("Error: number must be positive")
            sys.exit()
        
        if number > 10:
            print("Error: number must be less than 10")
            sys.exit()
        
        if number % 2 == 0:
            print("Error: number must be even")
            sys.exit()
    
    print("Done.")
    
