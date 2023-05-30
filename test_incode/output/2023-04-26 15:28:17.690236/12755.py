#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits and returns words. """    
    
    import sys
    
    fruits = sys.argv[1:]
    
    for fruit in fruits:
        words = 