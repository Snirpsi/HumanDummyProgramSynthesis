#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words or returns a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        words_to_remove = sys.argv[1]
        
        removed = remove