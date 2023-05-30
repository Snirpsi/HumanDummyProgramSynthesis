#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of numbers or enumerates words. """    
    import sys
    
    numbers = sys.argv[1:]
    
    for index, number in enumerate(numbers):
        print(index, number)
    
