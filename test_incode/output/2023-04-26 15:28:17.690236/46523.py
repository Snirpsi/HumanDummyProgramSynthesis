#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates numbers. """    
    
    import sys
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        print(number)
    
