#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds numbers or returns a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python add.py <number> <number> ... ")
        sys.exit()
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        print(number + 