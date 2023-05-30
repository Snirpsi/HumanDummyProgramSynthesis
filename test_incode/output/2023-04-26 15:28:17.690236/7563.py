#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints fruits or converts a list of words. """    
    import sys
    
    words = sys.argv[1:]
    
    if len(words) == 0:
        print("Usage: python fru