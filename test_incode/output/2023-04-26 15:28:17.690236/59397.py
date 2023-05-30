#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores words or stores words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 wordstore.py [words]")
        exit(1)
    
    words = sys.argv[1].split()
    
    storeWords(words)
    
