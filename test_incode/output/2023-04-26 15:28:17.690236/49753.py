#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of words. """    
    import sys
    words = sys.argv[1:]
    
    words = list(set(words))
    
    words.sort()
    
    for word in words:
        print(word)
    
