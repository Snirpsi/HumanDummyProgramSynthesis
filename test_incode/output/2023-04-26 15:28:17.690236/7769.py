#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words or enumerates words. """    
    import sys
    
    words = sys.argv[1:]
    
    words = [word.strip() for word in words]
    
    words = list(set(words))
    
    words.sort()
    
    for word in words:
        print(word)
    
