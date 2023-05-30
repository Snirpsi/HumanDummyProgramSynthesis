#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a port or returns a list of words. """    
    
    port = None
    
    if sys.argv[1] == 'open':
        port = open