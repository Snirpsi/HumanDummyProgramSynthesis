#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints numbers. """    
    import sys
    numbers = list(map(int, sys.stdin.read().split()))
    print(numbers)
    
