#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words. """    
    import sys
    
    words = sys.argv[1:]
    
    words = words.split()
    
    words = [w for w in words if w not in 