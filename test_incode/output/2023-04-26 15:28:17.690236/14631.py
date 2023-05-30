#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens numbers or multiplyes a list of numbers. """    
    
    import sys
    
    numbers = sys.argv[1:]
    
    if len(numbers) == 0:
        print("Usage: python 