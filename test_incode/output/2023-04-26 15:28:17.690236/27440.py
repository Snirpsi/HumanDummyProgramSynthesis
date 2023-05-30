#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers. """    
    import sys
    
    numbers = list(map(int, sys.stdin.read().split()))
    
    numbers_converted = []
    
    for number in numbers:
        numbers_converted.append(number * 2)
    
    print(" ".join(map(str, numbers_converted)))
    
