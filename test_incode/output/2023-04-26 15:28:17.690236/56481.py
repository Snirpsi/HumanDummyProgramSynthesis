#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds numbers or converts a list of numbers. """    
    import sys
    
    numbers = sys.argv[1:]
    
    if len(numbers) == 0:
        print("Usage: %s <numbers> [<numbers>]" % sys.argv[0])
        sys.exit()
    
    for number in numbers:
        try:
            number = int(number)
        except ValueError:
            print("Error: %s is not a number" % number)
            sys.exit()
        
        if number > 0:
            print(number)
        else:
            print("Error: %s cannot be negative" % number)
            sys.exit()
    
    if len(numbers) > 1:
        for number in numbers[1:]:
            try:
                number = int(number)
            except ValueError:
                print("Error: %s is not a number" % number)
                sys.exit()
            
            if number > 0:
                print(number)
            else:
                print("Error: %s cannot be negative" % number)
                sys.exit