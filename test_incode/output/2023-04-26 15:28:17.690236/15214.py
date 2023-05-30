#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts user input or prints a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8080
    
    