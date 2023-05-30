#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns numbers or opens a list of words. """    
    
    import sys
    
    words = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    
    numbers = 