#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over numbers or enumerates user input. """    
    
    import sys
    
    # Iterate over numbers or enumerate user input
    for arg in sys.argv[1:]:
        print(arg)
    
