#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers and removes numbers. """    
    import sys
    numbers = map(int, sys.stdin.readline().split())
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    print(" ".join(map(str, numbers)))
    
