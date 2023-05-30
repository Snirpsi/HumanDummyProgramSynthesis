#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers. """    
    
    # Read command line arguments
    numbers = sys.argv[1:]
    
    # Remove all numbers from list
    numbers = [x for x in numbers if x not in 