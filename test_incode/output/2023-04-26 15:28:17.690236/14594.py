#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns numbers. """    
    import sys
    numbers = [int(x) for x in sys.stdin.read().split()]
    print(numbers)
    
