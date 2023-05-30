#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of words. """    
    import sys
    
    words = sys.argv[1:]
    
    words = [w.strip() for w in words]
    
    words = list(set(words))
    
    words.sort()
    
    print(words)
    
