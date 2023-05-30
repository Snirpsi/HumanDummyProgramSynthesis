#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts words. """    
    import sys
    
    words = []
    for line in sys.stdin:
        words.append(line.strip())
    
    words = list(set(words))
    
    words.sort()
    
    words = [w for w in words if len(w) > 1]
    
    print(" ".join(words))
    
