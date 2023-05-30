#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words and adds words. """    
    import sys
    
    words = []
    
    for arg in sys.argv[1:]:
        words.append(arg)
    
    words = list(set(words))
    
    for word in words:
        print(word)
    
