#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words and multiplyes words. """    
    import sys
    
    words = [x.strip() for x in sys.stdin.read().split()]
    
    words = [x for x in words if x]
    
    words = [x*