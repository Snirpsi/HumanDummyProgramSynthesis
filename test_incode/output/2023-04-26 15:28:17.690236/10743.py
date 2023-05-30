#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words and removes numbers. """    
    
    import sys
    
    words = sys.argv[1:]
    
    words = [w.lower() for w in words]
    
    words = [w for w in words if len(w) > 1]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w in 