#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words and returns words. """    
    import sys
    
    words = []
    for word in sys.argv[1:]:
        words.append(word)
    
    words.sort()
    
    for word in words:
        print(word)
    
