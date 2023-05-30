#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers. """    
    
    import sys
    
    while True:
        try:
            n = int(sys.argv[1])
        except ValueError:
            print('Usage: python 