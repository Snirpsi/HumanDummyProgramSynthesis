#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes words and multiplyes a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    words = sys.argv[2:]
    
    words = [w for w in words if w != '']
    
    words = [w for w in words if w != '