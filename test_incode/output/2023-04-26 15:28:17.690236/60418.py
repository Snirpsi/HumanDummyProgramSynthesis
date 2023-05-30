#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers and converts a port. """    
    
    # Read input from stdin
    numbers = sys.stdin.read().split()
    
    # Remove numbers from list
    numbers = [x for x in numbers if x not in 