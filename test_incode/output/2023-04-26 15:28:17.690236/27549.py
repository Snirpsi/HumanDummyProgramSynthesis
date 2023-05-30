#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        sys.exit("Usage: %s <numbers>" % sys.argv[0])
    
    numbers = sys.argv[1:]
    
    numbers_