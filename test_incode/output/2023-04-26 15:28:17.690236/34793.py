#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over numbers or adds words. """    
    import sys
    
    # Read numbers from STDIN
    numbers = map(int, sys.stdin.readlines())
    
    # Add words to numbers
    numbers = map(lambda x: x + ' 