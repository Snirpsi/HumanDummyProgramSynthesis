#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of numbers. """    
    import sys
    numbers = sys.argv[1:]
    numbers = list(map(int, numbers))
    numbers.extend(range(10, 100