#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of words or iterates over words. """    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = sys.stdin.read().split()
    
    words = [w.lower() for w in words]
    
    for word in words:
        print(word)
    
