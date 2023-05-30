#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns numbers. """    
    import sys
    
    numbers = map(int, sys.stdin.readline().split())
    
    print(sum(numbers))

<|/ file filename=