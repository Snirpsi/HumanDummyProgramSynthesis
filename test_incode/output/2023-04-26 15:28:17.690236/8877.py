#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds numbers. """    
    import sys
    
    numbers = map(int, sys.stdin.read().split())
    
    for number in numbers:
        print(number + 