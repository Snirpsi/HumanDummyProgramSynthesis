#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores numbers or converts words. """    
    import sys
    
    words = []
    
    for arg in sys.argv[1:]:
        if arg == '--numbers':
            words = list(map(int, sys.stdin.read().split()))
        elif arg == '--words':
            words = list(map(str.strip, sys.stdin.read().split()))
        else:
            words.append(arg)
    
    print(" ".join(words))
    
