#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers or enumerates a list of numbers. """    
    
    import sys
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        print(number)
    
