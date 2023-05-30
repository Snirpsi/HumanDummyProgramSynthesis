#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words. """    
    import sys
    
    words = [w for w in sys.stdin.read().split()]
    
    print(" ".join(words))
    
