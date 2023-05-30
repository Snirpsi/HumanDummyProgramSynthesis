#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <fruit>" % sys.argv[0])
        sys.exit(1)
    
    fruit = sys.argv[1]
    
    fruits = 