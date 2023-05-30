#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds numbers. """    
    
    numbers = [int(x) for x in input().split()]
    
    for n in numbers:
        print(n + 