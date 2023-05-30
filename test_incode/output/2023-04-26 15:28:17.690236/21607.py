#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words. """    
    import sys
    
    words = []
    for word in sys.stdin:
        words.append(word)
    
    words.sort()
    
    for word in words:
        print(word, end=' ')
    
