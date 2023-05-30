#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts user input. """    
    
    # Parse command line arguments
    args = sys.argv[1:]
    
    # Print help if necessary
    if len(args) == 0:
        print('Usage: python 