#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints numbers and iterates over numbers. """    
    import sys
    
    numbers = list(map(int, sys.stdin.readline().split()))
    
    for number in numbers:
        print(number)
        
