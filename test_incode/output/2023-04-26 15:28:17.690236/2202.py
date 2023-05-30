#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        sys.exit("Usage: %s <filename>" % sys.argv[0])
    
    filename = sys.argv[1]
    
    web