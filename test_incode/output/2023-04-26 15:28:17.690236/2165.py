#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words and multiplyes a list of words. """    
    
    import sys
    
    words = []
    
    for word in sys.argv[1:]:
        words.append(word)
        
    words.sort()
    
    multiplied = []
    
    for word in words:
        multiplied.append(word*