#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of words. """    
    import sys
    words = []
    for line in sys.stdin:
        words.append(line.strip())
    
    words = set(words)
    
    words = sorted(words, key=len)
    
    print(" ".join(words))
    
