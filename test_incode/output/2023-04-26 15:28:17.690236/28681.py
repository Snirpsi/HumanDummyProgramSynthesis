#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words. """    
    import sys
    
    if len(sys.argv) > 1:
        words = [w.strip() for w in sys.argv[1].split(',')]
    else:
        words = ['python', '