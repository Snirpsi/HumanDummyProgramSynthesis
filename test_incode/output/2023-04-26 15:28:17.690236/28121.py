#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over user input. """    
    
    import sys
    
    # Iterate over user input
    for arg in sys.argv[1:]:
        print(arg)
    
