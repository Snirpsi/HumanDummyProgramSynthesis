#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words. """    
    
    import sys
    
    words = []
    
    for word in sys.argv[1:]:
        words.append(word.strip())
    
    words.sort()
    
    word