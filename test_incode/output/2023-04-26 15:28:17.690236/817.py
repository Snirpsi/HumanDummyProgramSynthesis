#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words or prints a list of words. """    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = 'hello'
    
    word