#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words. """    
    import sys
    
    words = [w.strip() for w in sys.argv[1:]]
    
    words.sort()
    
    for word in words:
        print(word)
    
    
