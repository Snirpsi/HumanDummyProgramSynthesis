#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts numbers or returns numbers. """    
    
    import sys
    
    numbers = sys.argv[1:]
    
    if len(numbers) == 0:
        print("Usage: python number_to_