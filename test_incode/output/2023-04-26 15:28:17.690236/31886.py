#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of words or returns words. """    
    
    import sys
    
    words = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    
    words = [word.lower() for word in words]
    
    print(" ".join(words))
    
