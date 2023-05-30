#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers. """    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: %s <numbers>' % sys.argv[0])
        sys.exit(1)
    
    numbers = map(int, sys.argv[1].split())
    
    numbers_