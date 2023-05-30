#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints all ports or enumerates fruits. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 0
    
    fruits = 