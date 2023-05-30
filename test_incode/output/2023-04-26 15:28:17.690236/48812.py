#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of words or stores user input. """    
    
    import sys
    
    words = sys.argv[1:]
    
    for word in words:
        print(word)
    
