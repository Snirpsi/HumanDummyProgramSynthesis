#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of numbers. """    
    import sys
    
    numbers = []
    
    if len(sys.argv) > 1:
        numbers = sys.argv[1:]
    
    for number in numbers:
        print(number)
    
