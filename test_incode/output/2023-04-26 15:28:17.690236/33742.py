#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits or enumerates a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        fruit = sys.argv[1]
    else:
        fruit = 'apple'
    
    fru