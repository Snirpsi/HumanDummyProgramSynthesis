#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers. """    
    
    import sys
    
    numbers = map(int, sys.stdin.readline().strip().split())
    
    for number in numbers:
        print(number)
    
