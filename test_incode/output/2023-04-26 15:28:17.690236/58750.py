#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words or converts a list of words. """    
    import sys
    
    if len(sys.argv) == 3:
        convert(sys.argv[1], sys.argv[2])
    else:
        convert(sys.argv[1])
    
