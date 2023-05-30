#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates user input and enumerates a list of words. """    
    
    import sys
    
    words = []
    
    for arg in sys.argv[1:]:
        words.append(arg)
    
    words = words + ['quit']
    
    for word in words:
        print(word)
    
    print('\nDone.')
    
