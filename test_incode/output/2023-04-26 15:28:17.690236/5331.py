#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes words. """    
    
    import sys
    
    words = [line.strip() for line in sys.stdin]
    
    removed = [word for word in words if word not in words]
    
    sys.stdout.write(" ".join(removed))
    
