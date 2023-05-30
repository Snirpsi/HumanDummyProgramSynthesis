#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers. """    
    import sys
    
    # Read command line arguments
    argv = sys.argv[1:]
    
    # Remove all numbers from argv
    argv = [x for x in argv if x != '']
    
    # Print the result
    print(' '.join(argv))

<|/ file filename=remove_numbers.py ext=.py |>