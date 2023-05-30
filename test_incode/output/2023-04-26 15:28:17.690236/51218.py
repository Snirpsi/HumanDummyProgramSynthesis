#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words or adds user input. """    
    import sys
    words = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    
    words = list(set(words))
    
    words.sort()
    
    print(" ".join(words))
    
