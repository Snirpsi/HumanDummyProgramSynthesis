#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words or removes words. """    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = sys.argv
    
    words = [w.strip() for w in words]
    
    words = [w for w in words if w]
    
    words = [w for w in words if not w.isdigit()]
    
    words = [w for w in words if not w in 