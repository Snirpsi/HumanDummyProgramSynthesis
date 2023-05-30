#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers. """    
    import sys
    
    numbers = map(int, sys.stdin.readline().split())
    
    numbers_sum = sum(numbers)
    
    print(numbers_sum)
    
