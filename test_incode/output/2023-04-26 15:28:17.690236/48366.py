#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words. """    
    import sys
    
    words = []
    for line in sys.stdin:
        words.append(line.strip())
    
    words.sort()
    
    word