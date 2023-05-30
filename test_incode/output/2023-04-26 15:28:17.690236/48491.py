#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers. """    
    import sys
    
    numbers = sys.argv[1:]
    
    if len(numbers) == 0:
        print("Usage: remove_number