#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of numbers or returns a list of numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 remove-numbers-from-a-list.py <number-list>")
        sys.exit()
    
    numbers = sys.argv[1].split()
    
    numbers_removed = remove