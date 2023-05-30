#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes words or adds words. """    
    
    # Get the command line arguments
    args = sys.argv[1:]
    
    # Print the help message
    if len(args) != 0:
        print('Usage: python 