#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        exit(1)
    
    words = sys.argv[1:]
    
    for word in words:
        print(word