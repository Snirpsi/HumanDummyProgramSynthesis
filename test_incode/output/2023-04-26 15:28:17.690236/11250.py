#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words. """    
    
    # Read input from stdin
    import sys
    
    # Remove words from stdin
    words = sys.stdin.read().split()
    
    # Print result
    print(" ".join(words))
    
