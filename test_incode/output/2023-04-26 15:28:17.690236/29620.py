#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words or iterates over user input. """    
    
    # Get the list of words from the command line
    words = sys.argv[1:]
    
    # Remove words from the list
    words = [w for w in words if w not in 