#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a port or multiplyes words. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: %s <words>" % sys.argv[0])
        exit(1)
    
    words = sys.argv[1:]
    
    for word in words:
        