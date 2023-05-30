#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds numbers. """    
    import sys
    numbers = map(int, sys.stdin.readlines())
    print(sum(numbers))
