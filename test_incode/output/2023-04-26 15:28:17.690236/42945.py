#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers or iterates over a list of numbers. """    
    import sys
    
    if len(sys.argv) > 1:
        list_to_ints(sys.argv[1])
    else:
        list_to_ints(sys.stdin)
    
