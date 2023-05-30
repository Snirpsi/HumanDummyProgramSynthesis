#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input or removes a list of words. """    
    
    # Get the command line arguments
    args = sys.argv[1:]
    
    # Remove any arguments not starting with '-'
    for arg in args:
        if arg[0] != '-':
            