#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a list of words or adds a list of words. """    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = []
    
    for word in words:
        print(word)
    
