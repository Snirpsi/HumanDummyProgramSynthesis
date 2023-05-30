#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens words or adds a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
        
        if word in 