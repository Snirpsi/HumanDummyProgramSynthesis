#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a port or iterates over numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 1
    
    for port in range(1,