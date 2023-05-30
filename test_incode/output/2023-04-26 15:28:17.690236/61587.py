#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words or multiplyes all ports. """    
    import sys
    
    words = []
    ports = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
        
    if len(sys.argv) > 2:
        ports = sys.argv[2:]
    
    if len(words) == 0:
        print('Usage: python 