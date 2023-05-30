#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of numbers or prints a port. """    
    import sys
    
    if len(sys.argv) > 1:
        numbers = sys.argv[1:]
        
        for number in numbers:
            print(number * 2)
    else:
        print("Usage: python multiplication.py <numbers>")
    
