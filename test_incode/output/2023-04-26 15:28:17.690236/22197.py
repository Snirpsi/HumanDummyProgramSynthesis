#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a port or stores numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 9999
    
    print("Port 