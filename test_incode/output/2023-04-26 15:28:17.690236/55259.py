#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of words or adds words. """    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = 