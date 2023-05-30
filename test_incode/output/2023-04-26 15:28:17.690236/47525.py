#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers and removes user input. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python remove-userinput.py <numbers>")
        sys.exit()
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        number = int(number)
        
        if number > 10:
            print("This number cannot be greater than 10")
            sys.exit()
        
        if number < 0:
            print("This number cannot be negative")
            sys.exit()
    
    print("All numbers have been removed")
    
    
