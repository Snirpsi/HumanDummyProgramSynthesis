#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input or returns a list of words. """    
    
    import sys
    
    words = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    
    words = [w.strip() for w in words]
    
    print(words)
    
    
