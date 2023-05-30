#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers or enumerates numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 enumerate_numbers.py <list>")
        sys.exit()
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        print(number)
    
