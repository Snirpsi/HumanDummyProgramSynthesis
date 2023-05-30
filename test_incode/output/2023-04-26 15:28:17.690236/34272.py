#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers or converts a list of numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python number_to_list.py <numbers>")
        sys.exit()
    
    numbers = sys.argv[1:]
    
    numbers = numbers.split(",")
    
    for number in numbers:
        try:
            number = int(number)
        except ValueError:
            print("Invalid number: %s" % number)
            sys.exit()
        
        if number < 0:
            print("Negative number: %s" % number)
            sys.exit()
        
        if number == 0:
            print("Empty number: %s" % number)
            sys.exit()
        
        if number > sys.maxsize:
            print("Number too big: %s" % number)
            sys.exit()
        
        print(number)
    
