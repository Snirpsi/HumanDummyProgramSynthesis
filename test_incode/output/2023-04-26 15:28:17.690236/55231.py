#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a list of words and removes words. """    
    import sys
    
    words = sys.argv[1:]
    
    words = [word for word in words if word not in 