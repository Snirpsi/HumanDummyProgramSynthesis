#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of words. """    
    
    import sys
    
    words = []
    for line in sys.stdin:
        words.extend(line.split())
    
    words = list(set(words))
    
    words.sort()
    
    sys.stdout.write(" ".join(words))
    
    