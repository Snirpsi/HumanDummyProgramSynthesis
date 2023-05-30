#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python addnumbers.py <numbers>")
        exit(1)
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        number = int(number)
        
        if number > 0:
            print(number + 