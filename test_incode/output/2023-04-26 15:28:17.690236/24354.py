#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of numbers. """    
    
    import sys
    
    numbers = [int(x) for x in sys.stdin.read().strip().split(' ')]
    
    