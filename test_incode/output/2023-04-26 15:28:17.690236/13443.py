#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers. """    
    import sys
    
    numbers = sys.argv[1:]
    
    numbers = [int(n) for n in numbers]
    
    numbers = sum(numbers, [])
    
    print(numbers)
    
