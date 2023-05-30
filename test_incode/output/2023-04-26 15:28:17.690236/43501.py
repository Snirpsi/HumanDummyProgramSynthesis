#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words and calculates a port. """    
    import sys
    
    words = sys.argv[1:]
    
    port = 0
    
    for word in words:
        port += int(word) * 