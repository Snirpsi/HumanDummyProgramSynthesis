#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns numbers and removes numbers. """    
    import sys
    numbers = sys.argv[1:]
    numbers = list(map(int, numbers))
    numbers.sort()
    numbers.remove