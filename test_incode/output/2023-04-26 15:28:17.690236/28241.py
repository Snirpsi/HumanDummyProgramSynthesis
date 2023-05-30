#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of numbers. """    
    import sys
    numbers = list(map(int, sys.stdin.read().split()))
    numbers.sort()
    for number in numbers:
        print(number)
