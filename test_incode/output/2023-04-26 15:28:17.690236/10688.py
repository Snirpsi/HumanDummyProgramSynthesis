#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: remove-word.py <word>")
        sys.exit()
    
    word = sys.argv[1]
    
    words = word.split()
    
    for word in words:
        if word in 