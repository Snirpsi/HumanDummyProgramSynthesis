#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns words or returns words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = 