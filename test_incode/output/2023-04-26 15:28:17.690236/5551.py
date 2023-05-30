#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port or calculates words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        
        words = []
        
        for word in 