#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of words. """    
    import sys
    
    words = []
    for line in sys.stdin:
        words.append(line.strip().lower())
    
    words = list(set(words))
    
    words.sort()
    
    sys.stdout.write(" ".join(words))
    
