#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words. """    
    import sys
    
    words = []
    for line in sys.stdin:
        words.append(line.strip())
    
    words.sort()
    
    print(" ".join(words))
    
