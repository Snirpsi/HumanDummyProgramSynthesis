#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words. """    
    import sys
    words = [word.strip() for word in sys.stdin.readlines()]
    
    words.sort()
    
    for word in words:
        print(word)
        
