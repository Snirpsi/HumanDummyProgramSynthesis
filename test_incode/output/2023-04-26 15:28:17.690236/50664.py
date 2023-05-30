#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of words or iterates over a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = sys.stdin.read().split()
    
    words = list(filter(None, words))
    
    for word in words:
        print(word)
    
