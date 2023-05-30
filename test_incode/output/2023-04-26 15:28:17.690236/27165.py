#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates user input and converts words. """    
    
    import sys
    
    words = []
    
    for word in sys.argv[1:]:
        words.append(word)
    
    for word in words:
        print(word)
    
