#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port or enumerates user input. """    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = input("Enter a port number: ")
    
    