#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints numbers. """    
    import sys
    
    numbers = list(map(int, sys.stdin.read().split()))
    
    for number in numbers:
        print(number)
        
    